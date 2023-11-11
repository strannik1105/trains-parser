import json
from interfaces.common.parser import IParser


class MockParser(IParser):
    def prepare_data(self, data):
        result_file = []
        for row in data:
            result_file.append(
                {
                    'wagnum': row[0],
                    'operdate': str(row[1]),
                    'desl_id': row[2],
                    'dest_id': row[3],
                    'train_id': row[4],
                }
            )
        return json.dumps(result_file)
