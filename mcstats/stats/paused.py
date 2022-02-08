from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'paused',
        {
            'unit': 'ticks',
        },
        mcstats.StatDiffReader(
            mcstats.StatReader(['minecraft:custom','minecraft:total_world_time']),
            mcstats.StatReader(['minecraft:custom','minecraft:play_time']) # 21w16a (data version 2711)
        )
    ))
