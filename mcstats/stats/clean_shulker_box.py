from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'clean_shulker_box',
        {
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:custom','minecraft:clean_shulker_box']),
        ])
    ))
