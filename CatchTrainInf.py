# coding:utf-8
# 東京メトロのAPIで運行情報をjson形式で取得する

import urllib.parse
import urllib.request

def trainInf():

    url = 'https://api.tokyometroapp.jp/api/v2/datapoints?'
    params = urllib.parse.urlencode(
            {'rdf:type':'odpt:TrainInformation',
             'acl:consumerKey':[アクセストークン],
            }
    )

    response = urllib.request.urlopen(url + params)
    return response.read()
