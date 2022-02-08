from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'talked_to_villager',
        {
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:talked_to_villager'])
    ))
