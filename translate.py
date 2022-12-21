#!/usr/bin/env python

import argparse

from googletrans import Translator

def main(text : str, to_lang : str = 'en') -> int:
    """This main function translates the text
    received as argument for the language
    passed to the parameter to_lang.

    """

    translator = Translator();

    translated_text = translator.translate(text, dest=to_lang);

    print(translated_text.text);

    return 0;

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(
                description='This program translates sentences said by person'
            );

    parser.add_argument(
                '--text',
                type=str,
                help='the sentences that you want to translate',
                required=True
            );

    parser.add_argument(
                '--to_lang',
                type=str,
                help='which language you want to translate',
                default='en'
            );

    args = parser.parse_args();

    message : str = args.text;
    to_lang : str = args.to_lang;

    exit(main(message, to_lang));
