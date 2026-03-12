import requests
import json
import xml.etree.ElementTree as ET

# API 網址 (回傳 XML)
url = "https://api.nlsc.gov.tw/idc/TextQueryRoad/H/遠東"

def fetch_data():
    try:
        response = requests.get(url)
        response.raise_for_status()

        # 設定編碼
        response.encoding = 'utf-8'
        xml_data = response.text

        # 解析 XML
        root = ET.fromstring(xml_data)

        # 將其轉為 list
        data_list = []

        for road in root.findall('textQueryRoad'):
            # 將同一筆資料的欄位組合在同一個字典中
            road_info = {
                "name": road.findtext('name'),
                "townCode": road.findtext('townCode'),
                "townName": road.findtext('townName')
            }
            data_list.append(road_info)

        # 儲存成 JSON
        with open("road_data.json", "w", encoding="utf-8") as f:
            json.dump(data_list, f, ensure_ascii=False, indent=4)

        print(f"成功擷取 {len(data_list)} 筆資料並儲存至 road_data.json")

    except Exception as e:
        print(f"發生錯誤：{e}")

if __name__ == "__main__":
    fetch_data()
