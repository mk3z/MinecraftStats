from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'open_shulker_box',
        {
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:custom','minecraft:open_shulker_box']),
        ])
    ))
