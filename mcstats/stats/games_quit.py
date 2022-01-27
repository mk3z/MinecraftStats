from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'games_quit',
        {
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:custom','minecraft:leave_game']),
        ])
    ))
