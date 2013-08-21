"""
spawningtool.constants
~~~~~~~~~~~~~~~~~~~~~~
"""

BO_EXCLUDED = set([
    'MULE',
    'ReaperPlaceholder',
    'Interceptor'
    'AutoTurret',
    'PointDefenseDrone',
    'Locust',
    'LocustMP',
    'Changeling',
    'InfestedTerran',
    'Overseer',
    'BroodLord',
    'Broodling',
    'BroodlingEscort',  # the guys that fly with the Brood Lord
    'Larva',
    'CreepTumor',
    'CreepTumorQueen',
    'InfestedTerransEgg',
    'AutoTurret',
    'InfestedTerran',
    'Interceptor',
    'SwarmHostBurrowed',
])

BUILD_TIMES = {
    'SCV': 17,
    'Marine': 25,
    'Marauder': 30,
    'Reaper': 40,
    'Ghost': 40,
    'BattleHellion': 30,  # Hellbat
    'Hellion': 30,
    'Hellbat': 30,
    'WidowMine': 40,
    'SiegeTank': 45,
    'Thor': 60,
    'Viking': 42,
    'Medivac': 42,
    'Raven': 60,
    'Banshee': 60,
    'Battlecruiser': 90,
    'Probe': 17,
    'Zealot': 38,
    'Stalker': 42,
    'Sentry': 37,
    'MothershipCore': 30,
    'HighTemplar': 55,
    'DarkTemplar': 55,
    'Immortal': 55,
    'Colossus': 75,
    'Archon': 12,
    'Observer': 30,
    'WarpPrism': 50,
    'Phoenix': 35,
    'VoidRay': 60,
    'Oracle': 50,
    'Tempest': 60,
    'Carrier': 120,
    'Drone': 17,
    'Queen': 50,
    'Zergling': 24,
    'Baneling': 20,
    'Roach': 27,
    'Hydralisk': 33,
    'SwarmHost': 40,
    'Infestor': 50,
    'Ultralisk': 55,
    'NydusWorm': 20,
    'NydusCanal': 20,
    'Overlord': 25,
    'Mutalisk': 33,
    'Corruptor': 40,
    'Viper': 40,
    # research
    'ZergMeleeWeaponsLevel1': 160,
    'ZergMeleeWeaponsLevel2': 190,
    'ZergMeleeWeaponsLevel3': 220,
    'ZergMissileWeaponsLevel1': 160,
    'ZergMissileWeaponsLevel2': 190,
    'ZergMissileWeaponsLevel3': 220,
    'ZergGroundArmorsLevel1': 160,
    'ZergGroundArmorsLevel2': 190,
    'ZergGroundArmorsLevel3': 220,
    'ZergFlyerWeaponsLevel1': 160,
    'ZergFlyerWeaponsLevel2': 190,
    'ZergFlyerWeaponsLevel3': 220,
    'ZergFlyerArmorsLevel1': 160,
    'ZergFlyerArmorsLevel2': 190,
    'ZergFlyerArmorsLevel3': 220,
    'zerglingmovementspeed': 110,
    'zerglingattackspeed': 130,
    'CentrificalHooks': 110,
    'GlialReconstitution': 110,
    'TunnelingClaws': 110,
    'hydraliskspeed': 80,  # Grooved Spines
    'HydraliskSpeedUpgrade': 100,  # Muscular Augments
    'overlordspeed': 60,
    'overlordtransport': 130,
    'Burrow': 100,
    'InfestorEnergyUpgrade': 80,
    'ChitinousPlating': 110,
    'LocustLifetimeIncrease': 120,
    'TerranInfantryWeaponsLevel1': 160,
    'TerranInfantryWeaponsLevel2': 190,
    'TerranInfantryWeaponsLevel3': 220,
    'TerranInfantryArmorsLevel1': 160,
    'TerranInfantryArmorsLevel2': 190,
    'TerranInfantryArmorsLevel3': 220,
    'TerranVehicleWeaponsLevel1': 160,
    'TerranVehicleWeaponsLevel2': 190,
    'TerranVehicleWeaponsLevel3': 220,
    'TerranVehicleArmorsLevel1': 160,
    'TerranVehicleArmorsLevel2': 190,
    'TerranVehicleArmorsLevel3': 220,
    'TerranShipWeaponsLevel1': 160,
    'TerranShipWeaponsLevel2': 190,
    'TerranShipWeaponsLevel3': 220,
    'TerranShipArmorsLevel1': 160,
    'TerranShipArmorsLevel2': 190,
    'TerranShipArmorsLevel3': 220,
    'TerranVehicleAndShipArmorsLevel1': 160,
    'TerranVehicleAndShipArmorsLevel2': 190,
    'TerranVehicleAndShipArmorsLevel3': 220,
    'Stimpack': 170,
    'PunisherGrenades': 60,
    'ShieldWall': 110,  # ? Combat Shield?
    'MedivacCaduceusReactor': 80,
    'PersonalCloaking': 120,
    'GhostMoebiusReactor': 80,
    'NeosteelFrame': 110,
    'HiSecAutoTracking': 80,
    'TerranBuildingArmor': 140,
    'BansheeCloak': 110,
    'DurableMaterials': 110,
    'RavenCorvidReactor': 110,
    'StrikeCannons': 110,
    'DrillClaws': 110,
    'TransformationServos': 110,
    'BattlecruiserBehemothReactor': 80,
    'ProtossGroundWeaponsLevel1': 160,
    'ProtossGroundWeaponsLevel2': 190,
    'ProtossGroundWeaponsLevel3': 220,
    'ProtossGroundArmorsLevel1': 160,
    'ProtossGroundArmorsLevel2': 190,
    'ProtossGroundArmorsLevel3': 220,
    'ProtossShieldsLevel1': 160,
    'ProtossShieldsLevel2': 190,
    'ProtossShieldsLevel3': 220,
    'ProtossAirWeaponsLevel1': 160,
    'ProtossAirWeaponsLevel2': 190,
    'ProtossAirWeaponsLevel3': 220,
    'ProtossAirArmorsLevel1': 160,
    'ProtossAirArmorsLevel2': 190,
    'ProtossAirArmorsLevel3': 220,
    'WarpGateResearch': 160,
    'BlinkTech': 170,
    'ObserverGraviticBooster': 80,
    'GraviticDrive': 80,
    'ExtendedThermalLance': 140,
    'Charge': 140,
    'PsiStormTech': 110,
    'PhoenixRangeUpgrade': 90,
    # unit change buildings
    'Lair': 80,
    'Hive': 100,
    'GreaterSpire': 150,
    'OrbitalCommand': 35,
    'PlanetaryFortress': 50,
    'Overseer': 17,
}

for key, value in BUILD_TIMES.iteritems():
    BUILD_TIMES[key] *= 16


TRACKED_ABILITIES = set([
    '250mmStrikeCannons',
    'BlindingCloud',
    'BuildAutoTurret',
    'CalldownMULE',
    'Contaminate',
    'Corruption',
    'EMPRound',
    'Feedback',
    'ForceField',
    'FungalGrowth',
    'GravitonBeam',
    'GuardianShield',
    'MassRecallMothership',
    'MothershipMassRecall',
    'MothershipCorePurifyNexus',
    'MassRecallMothershipCore',
    'InfestorNeuralParasite',
    'BuildPointDefenseDrone',
    'HallucinationArchon',
    'HallucinationColossus',
    'HallucinationHighTemplar',
    'HallucinationImmortal',
    'HallucinationPhoenix',
    'HallucinationProbe',
    'HallucinationStalker',
    'HallucinationVoidRay',
    'HallucinationWarpPrism',
    'HallucinationZealot',
    'PsionicStorm',
    'ScannerSweep',
    'SeekerMissile',
    'SniperRound',
    'SpawnLarva',
    'ExtraSupplies',
    'ChronoBoost',
    'QueenTransfusion',
    'YamatoGun',
    'Abduct',
    'TemporalField',
    'Envision',
    ])
