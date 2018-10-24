export LANG=en_US.UTF-8
#!/bin/bash

PWD=/home/shangwu/ecomBigData/script
cd $PWD

currentDate=`date "+%Y-%m-%d_%H%M%S"`

yesterday=`date -d yesterday +%Y%m%d`


if [ $# = 1 ] ; then 
	yesterday=$1
	echo "the date is $yesterday" 
else
	echo "the date is yesterday --$yesterday"
fi 

streamingDir=/opt/cloudera/parcels/CDH/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming.jar
mrInputDir=/user/RecOffline/preference_new/export/$yesterday/*[BC].lzo_deflate

mrOutputDir=/user/shangwu/ecomBigData/playMusicInfoTop/language/$yesterday

mapper=/home/shangwu/ecomBigData/map-red/getPalyMusicInfo_map_top.py
reducer=/home/shangwu/ecomBigData/map-red/getPalyMusicInfo_reduce_top_language.py

resourceMusic=/home/shangwu/ecomBigData/map-red/resource-music.txt
hadoop jar $streamingDir -mapper $mapper -reducer $reducer -file $mapper -file $reducer  -input $mrInputDir -output $mrOutputDir -file $resourceMusic -cmdenv "calTime=$yesterday"

hadoop fs -text $mrOutputDir/part-* >> $PWD/playMusicInfoTopLanguage.$yesterday

./createTableOn74.sh PlayMusicInfoTopLanguage $yesterday

/usr/bin/mysql -h192.168.211.74 -uroot -P5029  -D ecom_repository --skip-column-names --local-infile=1 -e "set @BH_REJECT_FILE_PATH = '/tmp/playMusicInfoTopLanguagefile.$yesterday';set @BH_ABORT_ON_THRESHOLD = 0.03;LOAD DATA LOCAL INFILE '$PWD/playMusicInfoTopLanguage.$yesterday' INTO TABLE PlayMusicInfoTopLanguage_$yesterday fields terminated by '\t';"

rm $PWD/playMusicInfoTopLanguage.$yesterday

echo "ALL DONE!"


http://blog.csdn.net/zhaoyl03/article/details/8657031/ 

hadoop jar /opt/cloudera/parcels/CDH/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.0.0-mr1-cdh4.6.0.jar -input /data/log/client/real/20160330/20160330_000000.log.hadoopEntry106.other.gz -output output2 -mapper cat -reducer wc

hadoop jar /opt/cloudera/parcels/CDH/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.0.0-mr1-cdh4.6.0.jar -file /data/client/code/py/mapper.py -mapper mapper.py -file /data/client/code/py/reducer.py -reducer reducer.py -input /data/log/client/real/20160330/* -output client/20160330/1005

$HADOOP_HOME/bin/hadoop jar /usr/hadoop2.0.0/share/hadoop/tools/lib/hadoop-streaming-2.0.0-cdh4.6.0.jar -file code/analyze/mapper.py -mapper mapper.py -file code/analyze/reducer.py -reducer reducer.py -input /user/20160324_040000.log.hadoopEntry106.other.gz -output out15



250:
 hadoop jar /opt/cloudera/parcels/CDH/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.0.0-mr1-cdh4.6.0.jar -input /data/log/client/real/20160330/* -output output7 -file mapper.py -file dispatcher.py -file RECOM_SHOW.py -file RECOM_RUN.py -file RECOM_START.py -file common_util.py -file REGDLL.py -file reducer.py -mapper mapper.py -reducer reducer.py