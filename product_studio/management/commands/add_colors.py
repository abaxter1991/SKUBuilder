from django.core.management.base import BaseCommand

from product_studio.models import Color


class Command(BaseCommand):
    help = 'Management command to create a base collection of colors.'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        color_map = {
            'Apple Green': 'GAPL',
            'Army Green': 'AGRN',
            'Banana Cream': 'BNACRM',
            'Black': 'BLK',
            'Blue': 'BLU',
            'Bondi Blue': 'BBLU',
            'Bone': 'BON',
            'Cardinal': 'CAR',
            'Charcoal': 'CHR',
            'Cream': 'CRM',
            'Dark Heather Gray': 'DHGRY',
            'Espresso': 'ESP',
            'Green': 'GRN',
            'Green Apple': 'GAPL',
            'Harvest Gold': 'HARGLD',
            'Heather Athletic': 'HATH',
            'Heather Charcoal': 'HCHR',
            'Heather Columbia Blue': 'HCBLU',
            'Heather Cool Blue': 'HCOOLBLU',
            'Heather Forest Green': 'HFORGRN',
            'Heather Gray': 'HGRY',
            'Heather Green': 'HGRN',
            'Heather Heavy Metal': 'HHM',
            'Heather Maroon': 'HMRN',
            'Heather Mauve': 'HMAV',
            'Heather Navy': 'HNVY',
            'Heather Neon Green': 'HNENGRN',
            'Heather Red': 'HRED',
            'Heather Teal': 'HTEL',
            'Hot Pink': 'HOTPNK',
            'Ice Blue': 'ICEBLU',
            'Indigo': 'IND',
            'Indigo Blue': 'IBLU',
            'Kelly Green': 'KGRN',
            'Light Olive': 'LOLV',
            'Lilac': 'LLC',
            'Lush': 'LSH',
            'Midnight Navy': 'MIDNVY',
            'Military Green': 'MGRN',
            'Mint': 'MNT',
            'Misty Blue': 'MBLU',
            'Navy': 'NVY',
            'Neon Yellow': 'NENYLW',
            'Olive': 'OLV',
            'Orange': 'ORG',
            'Plum': 'PLM',
            'Port': 'POR',
            'Purple Berry': 'PRPBRY',
            'Purple Rush': 'PRPRSH',
            'Raspberry': 'RSPBRY',
            'Red': 'RED',
            'Rose': 'ROS',
            'Royal': 'RBLU',
            'Royal Blue': 'RBLU',
            'Sand': 'SND',
            'Silk': 'SLK',
            'Stone Gray': 'STNGRY',
            'Storm': 'STRM',
            'Tahiti Blue': 'TAHBLU',
            'Tan': 'TAN',
            'Teal': 'TEL',
            'Turquoise': 'TRQS',
            'Warm Gray': 'WGRY',
            'White': 'WHT',
        }

        for color, sku in color_map.items():
            Color.objects.create_color(
                color=color,
                sku=sku,
            )
