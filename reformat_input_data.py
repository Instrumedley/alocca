import json

with open("input_raw_data.json", 'r') as json_file:
    json_decoded = json.load(json_file)
    #print(json_decoded)
    pk = 1

    fields = {}
    meta = {}

    json_data = []
    for element in json_decoded:
        fields = dict(name=element["name"],symbol=element['symbol'])
        meta['model'] = 'stock.Instrument'
        meta['pk'] = pk
        pk = pk + 1
        meta['fields'] = fields
        json_data.append(meta.copy())


    with open("input_format_data.json", 'w') as json_out_file:
        json.dump(json_data, json_out_file)