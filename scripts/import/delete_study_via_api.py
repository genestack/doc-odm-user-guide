#!/usr/bin/python

import argparse
import requests

BASE_URL = '/frontend/rs/genestack/studyCurator/default-released'

EXAMPLE_TEXT = '''example:

 python %(prog)s.py --srv https://qa.magnum.genestack.com --study GSF010529 GSF010530 --token <token>
 '''

def delete_study(study_accession, srv, token):
    app_endpoint = srv + '/frontend/endpoint/application/invoke/genestack/'
    url_authenticate = app_endpoint + 'signin/authenticateByApiToken'
    s = requests.Session()
    s.post(url_authenticate, json=[token])
    url_delete_object = app_endpoint + 'arvados-importer/wipeStudy'
    header = {'Genestack-API-Token': token}
    response = s.post(url=url_delete_object, json=[study_accession], headers=header)
    return response.status_code


def main():
    parser = argparse.ArgumentParser(prog='delete_study_via_api',
                                 description='Delete study',
                                 epilog=EXAMPLE_TEXT,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument('--srv', type=str, help='url of the server', required=True)
    parser.add_argument('--study', type=str, nargs='+', help='study accessions', required=True)
    parser.add_argument('--token', type=str, help='token', required=True)
    args = parser.parse_args()
    host = args.srv[:-1] if args.srv.endswith('/') else args.srv
    for acc in args.study:
        result = delete_study(acc, host, args.token)
        print(acc, result)


if __name__ == "__main__":
    main()

# python upload_study_and_samples.py --srv https://qa.magnum.genestack.com --study study_example_local.tsv --samples samples_example_local.final.tsv --aws_cred aws_cred.json --script_path '~/gits/work/unified/applications/odm-spots/scripts/dataloading/load_and_link_data_for_odm.py' --token tknPublic123
