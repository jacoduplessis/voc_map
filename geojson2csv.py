import json
import csv
import argparse
import pathlib


def main():


    parser = argparse.ArgumentParser()
    parser.add_argument('i', help='input files', nargs='+')
    
    args = parser.parse_args()

    for f in args.i:

        infile = pathlib.Path(f)

        geo = json.loads(infile.read_text())

        outfile = infile.parent / f'{infile.stem}.csv'

        with outfile.open(mode='w') as o:

            writer = csv.writer(o)
            writer.writerow(['name', 'longitude', 'latitude'])

            for ff in geo['features']:
                try:
                    name = ff['properties']['name']
                    lng, lat = ff['geometry']['coordinates']
                    writer.writerow([name, lng, lat])
                except Exception as e:
                    print(infile.stem)
                    print(ff)
                    print(e)
                    print('###')
                    continue

if __name__ == '__main__':
    main()

