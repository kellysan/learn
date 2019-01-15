#! /usr/bin/env python
# @Author : sanyapeng


old = ['meishuxuanchuan', 'kofgame', 'al', 'technology', 'repos2', 'ops', 'meishuchangjing', 'opc', 'zillionaire', 'ops_pass', 'kos', 'gsdemo', 'DemoGame', 'sea', 'zhujiange', 'offical', 'meishuyinxiao', 'achilles', 'xianpro', 'business', 'DM-game', 'Kogop', 'bai', 'shichangmeishu', 'ic', 'xianpro-art', 'saiyan', 'gm', 'developer', 'Heroes', 'Tyr', 'old_test', 'master', 'onepiece', 'product', 'guangxuan.bak', 'Vega', 'xianpro_deaprtment', 'backup', 'Heracles', 'inu', 'crius', 'DM_abandon_byzjf160719', 'VegaGame', 'ccc', 'orsk', 'Titan', 'slggame', 'treetfighter_art', 'DM_art_abandon_byzjf160719', 'kosart', 'operations']
new = ['DM-game', 'hr-public', 'kof-oversea-art', 'xianpro-art', 'gsdemo', 'war-asia', 'meishuyinxiao', 'testldap', 'war-kor-art', 'Titan', 'PM', 'offical', 'war-ui', 'DemoGame', 'kos', 'meishuchangjing', 'VegaGame', 'developer', 'BladeX', 'ic', 'xianpro', 'Vega', 'ops', 'technology', 'oplib', 'war-art-sourceFile', 'war-oversea', 'shichangmeishu', 'mini', 'achilles', 'repos2', 'xianpro_deaprtment', 'Heracles', 'sea', 'master', 'crius', 'meishuxuanchuan', 'hifive_total', 'opdata', 'kosart', 'art', 'Tyr', 'Heroes', 'inu-art', 'ops_pass', 'opc', 'ccc', 'achilles-art', 'tdr', 'war', 'inu', 'war_design', 'operations', 'phoenix', 'war-kor', 'filebak', 'logs', 'slggame', 'war-jan', 'war-asia-art', 'yunying', 'gaea', 'meishuzhongxin', 'war-art', 'orsk', 'kofgame', 'achilles-cache', 'treetfighter_art']

set1 = []

for i in old:
    if i not in new:
        print(i)
        set1.append(i)

print(set1)