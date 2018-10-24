import uuid
import json
import requests
import re
# import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager
import ssl


class InstagramReg:
	user_agent = "Instagram 12.0.0.16.90 (iPhone8,1; iOS 10_0_2; ru_RU; ru-RU; scale=2.00; gamut=normal; 750x1334) AppleWebKit/420+"
	baseApiUrl = "https://i.instagram.com/api/v1/"
	instasign_token = "a3ccdf3a-6773-4cc8-b77f-f1448d768770"  # Your InstaSign token from https://instasign.org/Panel

	def __init__(self, proxy=None):
		self.device_id = str(uuid.uuid4()).upper()
		self.waterfall_id = str(uuid.uuid4()).replace("-", "")
		self.proxy = proxy
		self.csrf_token = ""
		self.session = requests.Session()
		self.__configure_session()

	def __configure_session(self):
		headers = {
			"User-Agent": self.user_agent,
			"X-IG-Connection-Type": "WiFi",
			"X-IG-Capabilities": "36oX",
			"Accept-Language": "ru-RU;q=1, he-RU;q=0.9, en-RU;q=0.8",
			"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
			"Proxy-Connection": "keep-alive",
			"Accept": "*/*"
		}

		self.session.headers.update(headers)
		self.session.proxies = self.proxy
		self.session.verify = False

	@staticmethod
	def __get_csrf_token(request):
		return re.findall("csrftoken=(.*?);", request.headers["Set-Cookie"])[0]

	def sig_request(self, data):
		data = {
			"query": json.dumps(data),
			"token": self.instasign_token
		}
		try:
			response = requests.post("https://instasign.org/api/sign", data).text
		except BaseException, e:
			print e.message
			return
		return {"ig_sig_key_version": "4",
		        "signed_body": json.loads(response)["Data"]}

	def __request(self, method, data):
		response = self.session.post(self.baseApiUrl + method, data=data)
		self.csrf_token = self.__get_csrf_token(response)
		print(response.text)
		return response

	def __sync(self):
		data = {
			"id": self.device_id,
			"experiments": "ig_ios_reg_filled_button_universe,ig_ios_iconless_contactpoint,ig_ios_reg_redesign,"
			               "ig_ios_reg_flow_status_bar,ig_ios_email_phone_switcher_universe,enable_nux_language,"
			               "ig_ios_registration_robo_call_time,ig_ios_password_less_registration_universe,"
			               "ig_ios_one_click_login_universe_2,ig_ios_one_password_extension,ig_nonfb_sso_universe,"
			               "ig_ios_use_family_device_id_universe,ig_ios_universal_link_login,"
			               "ig_ios_one_click_login_tab_design_universe,ig_ios_iconless_username,"
			               "ig_ios_iconless_confirmation"
		}

		return self.__request("qe/sync/", self.sig_request(data))

	def __check_email(self, mail):
		data = {
			"qe_id": self.device_id,
			"email": mail,
			"_csrftoken": self.csrf_token
		}
		return self.__request("users/check_email/", self.sig_request(data))

	def __username_suggestions(self, username):
		data = {
			"waterfall_id": self.waterfall_id,
			"name": username,
			"_csrftoken": self.csrf_token
		}

		return self.__request("accounts/username_suggestions/", self.sig_request(data))

	def __create_account(self, username, password, email, first_name):
		data = {"password": password,
		        "device_id": self.device_id,
		        "email": email,
		        "waterfall_id": self.waterfall_id,
		        "username": username,
		        "_csrftoken": self.csrf_token,
		        "first_name": first_name}

		return self.__request("accounts/create/", self.sig_request(data))

	def create_new_account(self, username, password, email, first_name):
		self.__sync()
		'''
		self.__check_email(email)
		self.__username_suggestions(username)
		self.__create_account(username, password, email, first_name)
		'''


if __name__ == "__main__":
	reger = InstagramReg()

	# Creating new instagram account
	reger.create_new_account("newusername", "asdasd", "newusername@gmail.com", "Ivan")
