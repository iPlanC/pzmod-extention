'''
Author: PlanC14 planc2333@outlook.com
Date: 2022-05-28 11:04:52
LastEditors: PlanC14 planc2333@outlook.com
LastEditTime: 2022-05-28 12:03:06
FilePath: \pzmod-extention\tools\snippetsGen.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''

import csv
import json

itemFile = open('./item.csv', 'r', encoding='utf-8')
next(itemFile)

jsonT = """
{
	"pzmod init": {
		"prefix": "pzmod",
		"body": [
			"module ${1:} {",
			"    imports {",
			"        ${2:}",
			"    }",
			"    recipe ${3:} {",
			"        ",
			"    }",
			"    item ${4:} {",
			"        ",
			"    }",
			"}"
		],
		"description": [
			"生成一个mod结构",
			""
		]
	}
"""
with itemFile:
    reader = csv.reader(itemFile)
    for row in reader:
        jsonT = jsonT + ',"' + row[0] + '":' + '{"prefix": "' + row[0] + '", "body": ["' + row[0] + ' = ${1:' + row[2] + '},"], "description": ["' + row[1] + '", "' + row[2] + '"]}'
        # print(jsonT)
    jsonT = jsonT + "}"
    # print(json.dumps(json.loads(jsonT), indent=4, separators=(',', ': ')))
    with open('./snippets.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(json.loads(jsonT), indent=4, separators=(',', ': ')))
