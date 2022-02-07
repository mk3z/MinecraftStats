from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'use_chest',
        {
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:used','minecraft:chest']),
            mcstats.StatReader(['minecraft:used','minecraft:trapped_chest'])
        ])
    ))