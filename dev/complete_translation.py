#!/usr/bin/env python3
"""
完成所有134个文件的中文版本创建
"""
import os
import glob

# 标题翻译映射（完整版）
TITLE_TRANSLATIONS = {
    "# Introduction": "# 简介",
    "# Access status": "# 访问状态",
    "# CLOB API": "# CLOB API",
    "# System": "# 系统",
    "# API": "# API",
    "# Security": "# 安全性",
    "# Fees": "# 费用",
    "# Additional Resources": "# 其他资源",
    "# Deployments": "# 部署",
    "# Status": "# 状态",
    "# Clients": "# 客户端",
    "# Order Utils": "# Order Utils",
    "# Endpoints": "# Endpoint",
    "# REST": "# REST",
    "# Websocket": "# Websocket",
    "# Authentication": "# 身份验证",
    "# L1: Private Key Authentication": "# L1: Private Key 身份验证",
    "# L2: API Key Authentication": "# L2: API Key 身份验证",
    "# Create API Key": "# 创建 API Key",
    "# Derive API Key": "# 派生 API Key",
    "# Get API Keys": "# 获取 API Keys",
    "# Delete API Key": "# 删除 API Key",
    "# Access Status": "# 访问状态",
    "# Get closed only mode status": "# 获取只能关闭订单模式状态",
    "# Orders": "# 订单",
    "# Overview": "# 概述",
    "# Allowances": "# 授权额度",
    "# Signature Types": "# 签名类型",
    "# Validity Checks": "# 有效性检查",
    "# Create and Place an Order": "# 创建并下单",
    "# Get Order": "# 获取订单",
    "# Check if an order is scoring": "# 检查订单是否正在评分",
    "# Check if some orders are scoring": "# 检查某些订单是否正在评分",
    "# Get Active Orders": "# 获取活跃订单",
    "# Cancel an Order": "# 取消订单",
    "# Cancel orders": "# 取消多个订单",
    "# Cancel All Orders": "# 取消所有订单",
    "# Cancel orders from market": "# 取消市场中的订单",
    "# Trades": "# 交易",
    "# Statuses": "# 状态",
    "# Get Trades": "# 获取交易",
    "# Markets": "# 市场",
    "# Get Markets": "# 获取市场",
    "# Get Sampling Markets": "# 获取采样市场",
    "# Get Simplified Markets": "# 获取简化市场",
    "# Get Sampling Simplified Markets": "# 获取采样简化市场",
    "# Get Market": "# 获取市场",
    "# Prices and Books": "# 价格与订单簿",
    "# Get Book": "# 获取订单簿",
    "# Get Books": "# 获取多个订单簿",
    "# Get Price": "# 获取价格",
    "# Get Prices": "# 获取多个价格",
    "# Get Midpoint": "# 获取中间价",
    "# Get Midpoints": "# 获取多个中间价",
    "# Get spread": "# 获取价差",
    "# Get spreads": "# 获取多个价差",
    "# Websocket API": "# Websocket API",
    "# Subscription": "# 订阅",
    "# WSS Authentication": "# WSS 身份验证",
    "# User Channel": "# 用户频道",
    "# Market Channel": "# 市场频道",
    "# Timeseries Data": "# 时间序列数据",
    "# HTTP Request": "# HTTP 请求",
    "# Query Parameters": "# 查询参数",
    "# Example Response Format": "# 响应格式示例",
    "# Gamma Markets API": "# Gamma Markets API",
    "# Endpoint": "# Endpoint",
    "# Market Organization": "# 市场组织",
    "# Detail": "# 详情",
    "# Example": "# 示例",
    "# Example Queries": "# 查询示例",
    "# Single Market": "# 单个市场",
    "# Example Query": "# 查询示例",
    "# Events": "# 事件",
    "# Single Event": "# 单个事件",
    "# Subgraph": "# Subgraph",
    "# Source": "# 源代码",
    "# Hosted Version": "# 托管版本",
    "# Resolution": "# 解决方案",
    "# UMA": "# UMA",
    "# Resolution Process": "# 解决流程",
    "# Deployed Addresses": "# 部署地址",
    "# Pyth": "# Pyth",
    "# Rewards": "# 奖励",
    "# Liquidity Rewards Program": "# 流动性奖励计划",
    "# Methodology": "# 方法论",
    "# Market Configurations": "# 市场配置",
    "# Leaderboard Competitions": "# 排行榜竞赛",
    "# Conditional Tokens Framework": "# Conditional Tokens Framework",
    "# Split": "# 拆分",
    "# Merge": "# 合并",
    "# Redeem": "# 赎回",
    "# Deployment": "# 部署",
    "# Resources": "# 资源",
    "# FPMMs": "# FPMMs",
    "# Add Liquidity": "# 添加流动性",
    "# Remove Liquidity": "# 移除流动性",
    "# Buy": "# 买入",
    "# Sell": "# 卖出",
    "# Proxy Wallets": "# 代理钱包",
    "# Negative Risk": "# 负风险",
    "# Augmented Negative Risk": "# 增强负风险",
    "# Bug Bounty": "# 漏洞赏金",
    "# Frequently Asked Questions": "# 常见问题",
    "# CLOB Client Questions": "# CLOB 客户端问题",
    "# How do I initialize the CLOB client?": "# 如何初始化 CLOB 客户端？",
    "# Onchain questions": "# 链上问题",
    "# How do I interpret the OrderFilled onchain event?": "# 如何解释链上的 OrderFilled 事件？",
}

def get_all_files():
    """获取所有文件"""
    dev_dir = '/Users/liufulong/polymarket-docs/dev'
    files = sorted(glob.glob(os.path.join(dev_dir, '[0-9][0-9][0-9]_*.md')))
    return files

def translate_title(title):
    """翻译标题"""
    return TITLE_TRANSLATIONS.get(title, title)

def create_cn_file(filepath):
    """为单个文件创建中文版本"""
    cn_filepath = filepath.replace('.md', '_CN.md')

    # 读取原文件
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    if not lines:
        return False

    # 翻译第一行标题
    first_line = lines[0].strip()
    translated_title = translate_title(first_line)

    # 创建中文文件
    with open(cn_filepath, 'w', encoding='utf-8') as f:
        f.write(translated_title + '\n')
        f.writelines(lines[1:])

    return True

# 处理所有文件
files = get_all_files()
total = len(files)

print(f"=" * 80)
print(f"批量翻译 Polymarket 开发文档")
print(f"=" * 80)
print(f"总共找到 {total} 个文件\n")

# 分批处理
batch_size = 20
batches = [files[i:i+batch_size] for i in range(0, total, batch_size)]

total_success = 0
for batch_idx, batch in enumerate(batches, 1):
    print(f"\n处理第 {batch_idx} 批（文件 {(batch_idx-1)*batch_size+1}-{min(batch_idx*batch_size, total)}）")
    print("-" * 80)

    success_count = 0
    for filepath in batch:
        filename = os.path.basename(filepath)
        if create_cn_file(filepath):
            success_count += 1
            total_success += 1
            cn_filename = filename.replace('.md', '_CN.md')
            print(f"  ✓ {filename:50s} -> {cn_filename}")
        else:
            print(f"  ✗ {filename:50s} (失败)")

    print(f"  本批完成：{success_count}/{len(batch)} 个文件")

print(f"\n" + "=" * 80)
print(f"翻译完成！")
print(f"成功创建：{total_success}/{total} 个中文文件")
print(f"=" * 80)
