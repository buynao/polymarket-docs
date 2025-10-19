#!/usr/bin/env python3
"""
将翻译后的通用内容应用到所有134个中文文件
使用方法：
1. 先翻译 common_content_to_translate.md
2. 将翻译结果保存为 common_content_CN.md
3. 运行此脚本：python3 apply_translation_to_all.py
"""
import os
import glob

def apply_translation():
    """将翻译的通用内容应用到所有中文文件"""

    # 检查翻译文件是否存在
    cn_content_file = '/Users/liufulong/polymarket-docs/dev/common_content_CN.md'
    if not os.path.exists(cn_content_file):
        print("错误：找不到翻译文件 common_content_CN.md")
        print("请先翻译 common_content_to_translate.md 并保存为 common_content_CN.md")
        return False

    # 读取翻译的通用内容
    with open(cn_content_file, 'r', encoding='utf-8') as f:
        common_content_cn = f.read()

    # 获取所有中文文件
    dev_dir = '/Users/liufulong/polymarket-docs/dev'
    cn_files = sorted(glob.glob(os.path.join(dev_dir, '[0-9][0-9][0-9]_*_CN.md')))

    if not cn_files:
        print("错误：找不到中文文件")
        return False

    print(f"找到 {len(cn_files)} 个中文文件")
    print("开始应用翻译...\n")

    success_count = 0
    for i, filepath in enumerate(cn_files, 1):
        filename = os.path.basename(filepath)

        # 读取现有中文文件的第一行（已翻译的标题）
        with open(filepath, 'r', encoding='utf-8') as f:
            first_line = f.readline()

        # 写入：翻译的标题 + 翻译的通用内容
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(first_line)
            if not first_line.endswith('\n'):
                f.write('\n')
            f.write(common_content_cn)

        success_count += 1
        if i % 20 == 0 or i == len(cn_files):
            print(f"进度：{i}/{len(cn_files)} ({i*100//len(cn_files)}%)")

    print(f"\n完成！成功更新 {success_count} 个文件")
    return True

if __name__ == '__main__':
    print("="*80)
    print("应用翻译到所有中文文件")
    print("="*80 + "\n")

    if apply_translation():
        print("\n" + "="*80)
        print("翻译应用成功！")
        print("所有 134 个中文文件已更新为完整翻译版本")
        print("="*80)
    else:
        print("\n" + "="*80)
        print("翻译应用失败，请检查错误信息")
        print("="*80)
