import os
import opencc

def convert_s2t_file(filepath):
    converter = opencc.OpenCC('s2t')
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    converted_content = converter.convert(content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(converted_content)
    print(f"Translated {filepath}")

if __name__ == '__main__':
    files_to_translate = [
        'falv/legal_resources.md',
        'fly/media.md',
        'fuwu/government.md',
        'fuwu/universities.md',
        'README.md'
    ]
    for file in files_to_translate:
        convert_s2t_file(file)
