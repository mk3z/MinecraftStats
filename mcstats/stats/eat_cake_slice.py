from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'eat_cake_slice',
        {
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:custom','minecraft:eat_cake_slice']),
        ])
    ))
