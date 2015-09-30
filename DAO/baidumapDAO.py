# -*- coding:utf-8 -*-
__author__ = 'DreamCatcher'

import MySQLdb
import uuid

class BaiduMapDAO(object):
    def __init__(self,host= 'localhost',db='easygodb',user='root',password='1234'):
        self.host = 'localhost'
        self.db = 'baidumap'
        self.user='root'
        self.password = '1234'

    def savePOIData(self,data):
        db = MySQLdb.connect(self.host,self.user,self.password,self.db,charset='utf8')
        guid = uuid.uuid1()
        cursor = db.cursor()
        if 'results' not in data:
            return ;
        for poi in data['results']:
            name = poi['name']
            lat = poi['location']['lat']
            lng = poi['location']['lng']
            address = poi['address']
            uid = poi['uid']
            telephone = poi['telephone'] if 'telephone' in poi else ""
            if 'detail_info' in poi:
                type = poi['detail_info']['type'] if poi['detail_info'].has_key('type') else ""
                tag = poi['detail_info']['tag'] if poi['detail_info'].has_key('tag') else ""
                detail_url = poi['detail_info']['detail_url'] if poi['detail_info'].has_key('detail_url') else ""
                price = poi['detail_info']['price'] if poi['detail_info'].has_key('price') else ""
                shop_hours = poi['detail_info']['shop_hours'] if poi['detail_info'].has_key('shop_hours') else ""
                overall_rating = poi['detail_info']['overall_rating'] if poi['detail_info'].has_key('overall_rating') else ""
                taste_rating = poi['detail_info']['taste_rating'] if poi['detail_info'].has_key('taste_rating') else ""
                service_rating = poi['detail_info']['service_rating'] if poi['detail_info'].has_key('service_rating') else ""
                environment_rating = poi['detail_info']['environment_rating'] if poi['detail_info'].has_key('environment_rating') else ""
                facility_rating = poi['detail_info']['facility_rating'] if poi['detail_info'].has_key('facility_rating') else ""
                hygiene_rating = poi['detail_info']['hygiene_rating'] if poi['detail_info'].has_key('hygiene_rating') else ""
                technology_rating = poi['detail_info']['technology_rating'] if poi['detail_info'].has_key('technology_rating') else ""
                image_num = poi['detail_info']['image_num'] if poi['detail_info'].has_key('image_num') else ""
                comment_num = poi['detail_info']['comment_num'] if poi['detail_info'].has_key('comment_num') else ""
                favorite_num = poi['detail_info']['favorite_num'] if poi['detail_info'].has_key('favorite_num') else ""
                checkin_num = poi['detail_info']['checkin_num'] if poi['detail_info'].has_key('checkin_num') else ""
                groupon_num = poi['detail_info']['groupon_num'] if poi['detail_info'].has_key('groupon_num') else 0
                discount_num = poi['detail_info']['discount_num'] if poi['detail_info'].has_key('discount_num') else 0
            cursor.execute(\
                "insert into placepoi(guid,name,lat,lng,address,uid,telephone,type,tag,detail_url,price,shop_hours,overall_rating,taste_rating,service_rating,environment_rating,facility_rating,hygiene_rating,technology_rating,image_num,comment_num,favorite_num,checkin_num,groupon_num,discount_num)\
                values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (guid,name,lat,lng,address,uid,telephone,type,tag,detail_url,price,shop_hours,overall_rating,taste_rating,service_rating,environment_rating,facility_rating,hygiene_rating,technology_rating,image_num,comment_num,favorite_num,checkin_num,groupon_num,discount_num)
                )
            db.commit()
        cursor.close()
        db.close()
