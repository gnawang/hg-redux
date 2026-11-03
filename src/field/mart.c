#include "debug.h"
#include "types.h"

#include "constants/item.h"

#include "pokemon.h"
#include "save.h"
#include "script.h"

#ifdef MART_EXPANSION

struct MartItem {
    u16 item_id;
    u16 override_cost;
};

struct BadgeMartItems {
    u16 item_id;
    u8 required_badges;
};

// note: limited to 203 items (~34 pages)
const struct BadgeMartItems sBadgeMart[] = {
    { ITEM_POKE_BALL, 0 },
    { ITEM_GREAT_BALL, 3 },
    { ITEM_ULTRA_BALL, 5 },
    { ITEM_POTION, 0 },
    { ITEM_SUPER_POTION, 1 },
    { ITEM_HYPER_POTION, 5 },
    { ITEM_MAX_POTION, 7 },
    { ITEM_FULL_RESTORE, 8 },
    { ITEM_REVIVE, 3 },
    { ITEM_ANTIDOTE, 0 },
    { ITEM_PARALYZE_HEAL, 0 },
    { ITEM_AWAKENING, 1 },
    { ITEM_BURN_HEAL, 1 },
    { ITEM_ICE_HEAL, 1 },
    { ITEM_FULL_HEAL, 5 },
    { ITEM_ESCAPE_ROPE, 1 },
    { ITEM_REPEL, 1 },
    { ITEM_SUPER_REPEL, 3 },
    { ITEM_MAX_REPEL, 5 },
    // Redux additions
    { ITEM_MAX_ETHER, 3 },
    { ITEM_ELIXIR, 5 },
    { ITEM_MAX_ELIXIR, 7 },
    { ITEM_MAX_REVIVE, 8 },
};

void LONG_CALL InitMartUI(void *taskManager, FieldSystem *fieldSystem, const u16 *items, int kind, int buySell, int decoWhich, const struct MartItem *priceOverrides);

u16 sCherrygroveCityMart[] = {
    ITEM_AIR_MAIL, ITEM_HEAL_BALL, 0xFFFF
};

u16 sVioletCityMart[] = {
    ITEM_TUNNEL_MAIL, ITEM_HEAL_BALL, ITEM_NET_BALL,
    // Redux: newer TMs, supporting and niche moves
    ITEM_TM174, // Haze
    ITEM_TM096, // Eerie Impulse
    ITEM_TM223, // Metal Sound
    ITEM_TM216, // Feather Dance
    ITEM_TM213, // Coaching
    ITEM_TM173, // Charge
    0xFFFF
};

u16 sAzaleaCityMart[] = {
    ITEM_BLOOM_MAIL, ITEM_HEAL_BALL, ITEM_NET_BALL,
    // Redux: newer TMs, low-damage and support moves, and the terrains
    ITEM_TM176, // Sand Tomb
    ITEM_TM179, // Smack Down
    ITEM_TM193, // Weather Ball
    ITEM_TM211, // Electroweb
    ITEM_TM194, // Grassy Glide
    ITEM_TM122, // Encore
    ITEM_TM136, // Electric Terrain
    ITEM_TM137, // Grassy Terrain
    ITEM_TM139, // Misty Terrain
    ITEM_TM138, // Psychic Terrain
    0xFFFF
};

u16 sGoldenrodDepartmentUpper2F[] = {
    ITEM_POTION, ITEM_SUPER_POTION, ITEM_HYPER_POTION, ITEM_MAX_POTION, ITEM_REVIVE, ITEM_ANTIDOTE, ITEM_PARALYZE_HEAL, ITEM_BURN_HEAL, ITEM_ICE_HEAL, ITEM_AWAKENING, ITEM_FULL_HEAL,
    // Redux: PP Up, Ability Capsule/Patch and Nature Mints
    ITEM_PP_UP,
    ITEM_ABILITY_CAPSULE,
    ITEM_ABILITY_PATCH,
    ITEM_LONELY_MINT,
    ITEM_ADAMANT_MINT,
    ITEM_NAUGHTY_MINT,
    ITEM_BRAVE_MINT,
    ITEM_BOLD_MINT,
    ITEM_IMPISH_MINT,
    ITEM_LAX_MINT,
    ITEM_RELAXED_MINT,
    ITEM_MODEST_MINT,
    ITEM_MILD_MINT,
    ITEM_RASH_MINT,
    ITEM_QUIET_MINT,
    ITEM_CALM_MINT,
    ITEM_GENTLE_MINT,
    ITEM_CAREFUL_MINT,
    ITEM_SASSY_MINT,
    ITEM_TIMID_MINT,
    ITEM_HASTY_MINT,
    ITEM_JOLLY_MINT,
    ITEM_NAIVE_MINT,
    ITEM_SERIOUS_MINT,
    0xFFFF
};

u16 sGoldenrodDepartmentLower2F[] = {
    ITEM_POKE_BALL, ITEM_GREAT_BALL, ITEM_ULTRA_BALL, ITEM_ESCAPE_ROPE, ITEM_POKE_DOLL, ITEM_REPEL, ITEM_SUPER_REPEL, ITEM_MAX_REPEL, ITEM_GRASS_MAIL, ITEM_FLAME_MAIL, ITEM_BUBBLE_MAIL, ITEM_SPACE_MAIL, 0xFFFF
};

u16 sGoldenrodDepartment3F[] = {
    ITEM_X_SPEED, ITEM_X_ATTACK, ITEM_X_DEFENSE, ITEM_GUARD_SPEC, ITEM_DIRE_HIT, ITEM_X_ACCURACY, ITEM_X_SP_ATK, ITEM_X_SP_DEF,
    // Redux: evolution items (used directly on the Pokemon)
    ITEM_KINGS_ROCK,
    ITEM_METAL_COAT,
    ITEM_DRAGON_SCALE,
    ITEM_UP_GRADE,
    ITEM_DUBIOUS_DISC,
    ITEM_PROTECTOR,
    ITEM_ELECTIRIZER,
    ITEM_MAGMARIZER,
    ITEM_REAPER_CLOTH,
    ITEM_PRISM_SCALE,
    ITEM_DEEP_SEA_TOOTH,
    ITEM_DEEP_SEA_SCALE,
    ITEM_RAZOR_FANG,
    ITEM_RAZOR_CLAW,
    ITEM_OVAL_STONE,
    0xFFFF
};

u16 sGoldenrodDepartment4F[] = {
    ITEM_PROTEIN, ITEM_IRON, ITEM_CALCIUM, ITEM_ZINC, ITEM_CARBOS, ITEM_HP_UP, 0xFFFF
};

u16 sGoldenrodDepartment5F[] = {
    ITEM_TM070, ITEM_TM017, ITEM_TM054, ITEM_TM083, ITEM_TM016, ITEM_TM033, ITEM_TM022, ITEM_TM052, ITEM_TM038, ITEM_TM025, ITEM_TM014, ITEM_TM015,
    // Redux: newer TMs and TRs, medium-damage and niche moves, and the less useful TRs
    ITEM_TM222, // Breaking Swipe
    ITEM_TM219, // Skitter Smack
    ITEM_TM215, // Scorching Sands
    ITEM_TM228, // Psychic Noise
    ITEM_TM207, // Temper Flare
    ITEM_TM199, // Lash Out
    ITEM_TM00, // Mega Punch
    ITEM_TM134, // Reversal
    ITEM_TM121, // Heavy Slam
    ITEM_TM189, // Heat Crash
    ITEM_TM132, // Baton Pass
    ITEM_TR13, // Focus Energy
    ITEM_TR14, // Metronome
    ITEM_TR85, // Work Up
    ITEM_TR44, // Cosmic Power
    ITEM_TR91, // Venom Drench
    ITEM_TR80, // Electro Ball
    ITEM_TR82, // Stored Power
    ITEM_TR19, // Tri Attack
    ITEM_TR41, // Blaze Kick
    ITEM_TR01, // Body Slam
    // Redux: evolution stones
    ITEM_FIRE_STONE,
    ITEM_WATER_STONE,
    ITEM_THUNDER_STONE,
    ITEM_LEAF_STONE,
    ITEM_MOON_STONE,
    ITEM_SUN_STONE,
    ITEM_ICE_STONE,
    0xFFFF
};

u16 sGoldenrodHerbs[] = {
    ITEM_HEAL_POWDER, ITEM_ENERGY_POWDER, ITEM_ENERGY_ROOT, ITEM_REVIVAL_HERB, 0xFFFF
};

u16 sEcruteakMart[] = {
    ITEM_HEART_MAIL, ITEM_HEAL_BALL, ITEM_NET_BALL,
    // Redux: newer TMs, high-utility moves
    ITEM_TM196, // Flip Turn
    ITEM_TM188, // Scald
    ITEM_TM095, // Leech Life
    ITEM_TM187, // Icicle Spear
    ITEM_TM200, // Scale Shot
    ITEM_TM185, // Lunge
    ITEM_TM124, // Ice Spinner
    ITEM_TM221, // Throat Chop
    0xFFFF
};

u16 sOlivineMart[] = {
    ITEM_HEART_MAIL, ITEM_HEAL_BALL, ITEM_NET_BALL,
    // Redux: newer TMs, consistent, stronger attacks
    ITEM_TM197, // Dual Wingbeat
    ITEM_TM112, // Aura Sphere
    ITEM_TM212, // Triple Axel
    ITEM_TM162, // Bug Buzz
    ITEM_TM108, // Crunch
    ITEM_TM101, // Power Gem
    ITEM_TM106, // Drill Run
    ITEM_TM110, // Liquidation
    ITEM_TM218, // Expanding Force
    ITEM_TM131, // Pollen Puff
    0xFFFF
};

u16 sCianwoodPharmacy[] = {
    ITEM_POTION, ITEM_SUPER_POTION, ITEM_HYPER_POTION, ITEM_FULL_HEAL, ITEM_REVIVE, 0xFFFF
};

u16 sBlackthornAndBattleFrontierMart[] = {
    ITEM_AIR_MAIL, ITEM_NET_BALL, ITEM_DUSK_BALL,
    // Redux: newer TMs, strong attacks
    ITEM_TM186, // High Horsepower
    ITEM_TM127, // Play Rough
    ITEM_TM147, // Wild Charge
    ITEM_TM151, // Phantom Force
    ITEM_TM117, // Hyper Voice
    ITEM_TM209, // Muddy Water
    ITEM_TM214, // Sludge Wave
    ITEM_TM206, // Petal Blizzard
    0xFFFF
};

u16 sIndigoPlateau[] = {
    ITEM_ULTRA_BALL, ITEM_MAX_REPEL, ITEM_HYPER_POTION, ITEM_MAX_POTION, ITEM_FULL_RESTORE, ITEM_REVIVE, ITEM_FULL_HEAL,
    // Redux: newer TMs, strong attacks
    ITEM_TM204, // Double Edge
    ITEM_TM210, // Supercell Slam
    ITEM_TM201, // Misty Explosion
    ITEM_TM220, // Meteor Beam
    0xFFFF
};

u16 sVermilionAndSafariMart[] = {
    ITEM_AIR_MAIL, ITEM_NEST_BALL, ITEM_DUSK_BALL, ITEM_QUICK_BALL, 0xFFFF
};

u16 sSaffronMart[] = {
    ITEM_AIR_MAIL, ITEM_DUSK_BALL, ITEM_QUICK_BALL, 0xFFFF
};

u16 sLavenderMart[] = {
    ITEM_AIR_MAIL, ITEM_DUSK_BALL, ITEM_QUICK_BALL, 0xFFFF
};

u16 sCeruleanMart[] = {
    ITEM_AIR_MAIL, ITEM_QUICK_BALL, 0xFFFF
};

u16 sCeladonDepartmentUpper2F[] = {
    ITEM_POTION, ITEM_SUPER_POTION, ITEM_HYPER_POTION, ITEM_MAX_POTION, ITEM_REVIVE, ITEM_ANTIDOTE, ITEM_PARALYZE_HEAL, ITEM_BURN_HEAL, ITEM_ICE_HEAL, ITEM_AWAKENING, ITEM_FULL_HEAL,
    // Redux: PP Up, Ability Capsule/Patch and Nature Mints
    ITEM_PP_UP,
    ITEM_ABILITY_CAPSULE,
    ITEM_ABILITY_PATCH,
    ITEM_LONELY_MINT,
    ITEM_ADAMANT_MINT,
    ITEM_NAUGHTY_MINT,
    ITEM_BRAVE_MINT,
    ITEM_BOLD_MINT,
    ITEM_IMPISH_MINT,
    ITEM_LAX_MINT,
    ITEM_RELAXED_MINT,
    ITEM_MODEST_MINT,
    ITEM_MILD_MINT,
    ITEM_RASH_MINT,
    ITEM_QUIET_MINT,
    ITEM_CALM_MINT,
    ITEM_GENTLE_MINT,
    ITEM_CAREFUL_MINT,
    ITEM_SASSY_MINT,
    ITEM_TIMID_MINT,
    ITEM_HASTY_MINT,
    ITEM_JOLLY_MINT,
    ITEM_NAIVE_MINT,
    ITEM_SERIOUS_MINT,
    0xFFFF
};

u16 sCeladonDepartmentLower2F[] = {
    ITEM_POKE_BALL, ITEM_GREAT_BALL, ITEM_ULTRA_BALL, ITEM_ESCAPE_ROPE, ITEM_POKE_DOLL, ITEM_REPEL, ITEM_SUPER_REPEL, ITEM_MAX_REPEL, ITEM_GRASS_MAIL, ITEM_FLAME_MAIL, ITEM_BUBBLE_MAIL, ITEM_SPACE_MAIL, 0xFFFF
};

u16 sCeladonDepartment3F[] = {
    ITEM_TM021, ITEM_TM027, ITEM_TM087, ITEM_TM078, ITEM_TM012, ITEM_TM041, ITEM_TM020, ITEM_TM028, ITEM_TM076, ITEM_TM055, ITEM_TM072, ITEM_TM079,
    // Redux: newer TMs and TRs, the strongest attacks, and the stronger TRs
    ITEM_TM167, // Close Combat
    ITEM_TM164, // Brave Bird
    ITEM_TM217, // Future Sight
    ITEM_TM142, // Hydro Pump
    ITEM_TM198, // Poltergeist
    ITEM_TM159, // Leaf Storm
    ITEM_TM165, // Flare Blitz
    ITEM_TM160, // Hurricane
    ITEM_TM190, // Solar Blade
    ITEM_TM170, // Steel Beam
    ITEM_TR12, // Agility
    ITEM_TR23, // Spikes
    ITEM_TR54, // Toxic Spikes
    ITEM_TR25, // Psyshock
    ITEM_TR97, // Psychic Fangs
    ITEM_TR92, // Dazzling Gleam
    ITEM_TR93, // Darkest Lariat
    ITEM_TR81, // Foul Play
    ITEM_TR50, // Leaf Blade
    ITEM_TR99, // Body Press
    ITEM_TR28, // Megahorn
    ITEM_TR72, // Power Whip
    // Redux: late-game stones and items for later evolutions of Gen 1-4 Pokemon (Kleavor, Ursaluna)
    ITEM_SHINY_STONE,
    ITEM_DUSK_STONE,
    ITEM_DAWN_STONE,
    ITEM_BLACK_AUGURITE,
    ITEM_PEAT_BLOCK,
    0xFFFF
};

u16 sCeladonDepartment4F[] = {
    ITEM_AIR_MAIL, ITEM_TUNNEL_MAIL, ITEM_BLOOM_MAIL, 0xFFFF
};

u16 sCeladonDepartmentLeft5F[] = {
    ITEM_X_SPEED, ITEM_X_ATTACK, ITEM_X_DEFENSE, ITEM_GUARD_SPEC, ITEM_DIRE_HIT, ITEM_X_ACCURACY, ITEM_X_SP_ATK, ITEM_X_SP_DEF, 0xFFFF
};

u16 sCeladonDepartmentRight5F[] = {
    ITEM_PROTEIN, ITEM_IRON, ITEM_CALCIUM, ITEM_ZINC, ITEM_CARBOS, ITEM_HP_UP, 0xFFFF
};

u16 sFuschiaMart[] = {
    ITEM_STEEL_MAIL, ITEM_DUSK_BALL, ITEM_QUICK_BALL, 0xFFFF
};

u16 sPewterMart[] = {
    ITEM_STEEL_MAIL, ITEM_NEST_BALL, ITEM_QUICK_BALL, 0xFFFF
};

u16 sViridianMart[] = {
    ITEM_STEEL_MAIL, ITEM_NET_BALL, ITEM_HEAL_BALL, 0xFFFF
};

u16 sMtMoonSquare[] = {
    ITEM_POKE_DOLL, ITEM_FRESH_WATER, ITEM_SODA_POP, ITEM_LEMONADE, ITEM_REPEL, ITEM_HEART_MAIL, 0xFFFF
};

u16 sMahoganyPreRocketHideout[] = {
    ITEM_TINY_MUSHROOM, ITEM_POKE_BALL, ITEM_POTION, 0xFFFF
};

u16 sMahoganyPostRocketHideout[] = {
    ITEM_GREAT_BALL, ITEM_SUPER_POTION, ITEM_HYPER_POTION, ITEM_ANTIDOTE, ITEM_PARALYZE_HEAL, ITEM_SUPER_REPEL, ITEM_REVIVE, ITEM_AIR_MAIL,
    // Redux: newer TMs, setup moves
    ITEM_TM100_SV, // Dragon Dance
    ITEM_TM140, // Nasty Plot
    ITEM_TM128, // Amnesia
    ITEM_TM224, // Curse
    0xFFFF
};

BOOL ScrCmd_MartBuy(SCRIPTCONTEXT *ctx)
{
    u16 unused UNUSED = ScriptGetVar(ctx);

    u16 items[NELEMS(sBadgeMart) + 1];
    u8 badgeCount = 0;
    u8 index = 0;
    u32 i;

    for (i = 0; i < 16; i++) {
        if (PlayerProfile_TestBadgeFlag(Sav2_PlayerData_GetProfileAddr(ctx->fsys->savedata), i) == TRUE) {
            badgeCount++;
        }
    }

    for (i = 0; i < NELEMS(sBadgeMart); i++) {
        if (badgeCount >= sBadgeMart[i].required_badges) {
            items[index] = sBadgeMart[i].item_id;
            index++;
        }
    }

    items[index] = 0xFFFF;
    InitMartUI(ctx->taskman, ctx->fsys, items, 0, 0, 0, 0); // this doesn't honor price overrides
    return TRUE;
}

#endif // MART_EXPANSION

#ifdef POKEATHLON_SHOP_EXPANSION

const struct MartItem sPokeathlonShop_Sunday[] = {
    { ITEM_RED_APRICORN, 200 },
    { ITEM_BLUE_APRICORN, 200 },
    { ITEM_BLACK_APRICORN, 200 },
    { ITEM_MOOMOO_MILK, 100 },
    { ITEM_KINGS_ROCK, 3000 },
    { ITEM_HEART_SCALE, 1000 },
    { 0xFFFF, 0 },
};

const struct MartItem sPokeathlonShop_Monday[] = {
    { ITEM_RED_APRICORN, 200 },
    { ITEM_BLUE_APRICORN, 200 },
    { ITEM_GREEN_APRICORN, 200 },
    { ITEM_MOOMOO_MILK, 100 },
    { ITEM_MOON_STONE, 3000 },
    { ITEM_RARE_CANDY, 2000 },
    { 0xFFFF, 0 },
};

const struct MartItem sPokeathlonShop_Tuesday[] = {
    { ITEM_YELLOW_APRICORN, 200 },
    { ITEM_PINK_APRICORN, 200 },
    { ITEM_WHITE_APRICORN, 200 },
    { ITEM_MOOMOO_MILK, 100 },
    { ITEM_FIRE_STONE, 2500 },
    { ITEM_PP_UP, 1000 },
    { 0xFFFF, 0 },
};

const struct MartItem sPokeathlonShop_Wednesday[] = {
    { ITEM_BLUE_APRICORN, 200 },
    { ITEM_PINK_APRICORN, 200 },
    { ITEM_BLACK_APRICORN, 200 },
    { ITEM_MOOMOO_MILK, 100 },
    { ITEM_WATER_STONE, 2500 },
    { ITEM_HEART_SCALE, 1000 },
    { 0xFFFF, 0 },
};

const struct MartItem sPokeathlonShop_Thursday[] = {
    { ITEM_YELLOW_APRICORN, 200 },
    { ITEM_PINK_APRICORN, 200 },
    { ITEM_WHITE_APRICORN, 200 },
    { ITEM_MOOMOO_MILK, 100 },
    { ITEM_THUNDER_STONE, 2500 },
    { ITEM_PP_UP, 1000 },
    { 0xFFFF, 0 },
};

const struct MartItem sPokeathlonShop_Friday[] = {
    { ITEM_RED_APRICORN, 200 },
    { ITEM_YELLOW_APRICORN, 200 },
    { ITEM_GREEN_APRICORN, 200 },
    { ITEM_MOOMOO_MILK, 100 },
    { ITEM_METAL_COAT, 2500 },
    { ITEM_NUGGET, 500 },
    { 0xFFFF, 0 },
};

const struct MartItem sPokeathlonShop_Saturday[] = {
    { ITEM_GREEN_APRICORN, 200 },
    { ITEM_WHITE_APRICORN, 200 },
    { ITEM_BLACK_APRICORN, 200 },
    { ITEM_MOOMOO_MILK, 100 },
    { ITEM_LEAF_STONE, 2500 },
    { ITEM_RARE_CANDY, 2000 },
    { 0xFFFF, 0 },
};

const struct MartItem sPokeathlonShop_NatdexSunday[] = {
    { ITEM_RED_APRICORN, 200 },
    { ITEM_BLUE_APRICORN, 200 },
    { ITEM_BLACK_APRICORN, 200 },
    { ITEM_MOOMOO_MILK, 100 },
    { ITEM_KINGS_ROCK, 3000 },
    { ITEM_HEART_SCALE, 1000 },
    { ITEM_FULL_RESTORE, 500 },
    { ITEM_NUGGET, 500 },
    { ITEM_SUN_STONE, 3000 },
    { ITEM_FIRE_STONE, 2500 },
    { ITEM_SHINY_STONE, 3000 },
    { ITEM_DAWN_STONE, 3000 },
    { 0xFFFF, 0 },
};

const struct MartItem sPokeathlonShop_NatdexMonday[] = {
    { ITEM_RED_APRICORN, 200 },
    { ITEM_BLUE_APRICORN, 200 },
    { ITEM_GREEN_APRICORN, 200 },
    { ITEM_MOOMOO_MILK, 100 },
    { ITEM_MOON_STONE, 3000 },
    { ITEM_RARE_CANDY, 2000 },
    { ITEM_FULL_RESTORE, 500 },
    { ITEM_KINGS_ROCK, 3000 },
    { ITEM_SUN_STONE, 3000 },
    { ITEM_WATER_STONE, 2500 },
    { ITEM_SHINY_STONE, 3000 },
    { ITEM_DUSK_STONE, 3000 },
    { 0xFFFF, 0 },
};

const struct MartItem sPokeathlonShop_NatdexTuesday[] = {
    { ITEM_YELLOW_APRICORN, 200 },
    { ITEM_PINK_APRICORN, 200 },
    { ITEM_WHITE_APRICORN, 200 },
    { ITEM_MOOMOO_MILK, 100 },
    { ITEM_FIRE_STONE, 2500 },
    { ITEM_PP_UP, 1000 },
    { ITEM_FULL_RESTORE, 500 },
    { ITEM_METAL_COAT, 2500 },
    { ITEM_WATER_STONE, 2500 },
    { ITEM_LEAF_STONE, 2500 },
    { ITEM_DUSK_STONE, 3000 },
    { ITEM_DAWN_STONE, 3000 },
    { 0xFFFF, 0 },
};

const struct MartItem sPokeathlonShop_NatdexWednesday[] = {
    { ITEM_BLUE_APRICORN, 200 },
    { ITEM_PINK_APRICORN, 200 },
    { ITEM_BLACK_APRICORN, 200 },
    { ITEM_MOOMOO_MILK, 100 },
    { ITEM_WATER_STONE, 2500 },
    { ITEM_HEART_SCALE, 1000 },
    { ITEM_FULL_RESTORE, 500 },
    { ITEM_DRAGON_SCALE, 2500 },
    { ITEM_THUNDER_STONE, 2500 },
    { ITEM_MOON_STONE, 3000 },
    { ITEM_SHINY_STONE, 3000 },
    { ITEM_DAWN_STONE, 3000 },
    { 0xFFFF, 0 },
};

const struct MartItem sPokeathlonShop_NatdexThursday[] = {
    { ITEM_YELLOW_APRICORN, 200 },
    { ITEM_PINK_APRICORN, 200 },
    { ITEM_WHITE_APRICORN, 200 },
    { ITEM_MOOMOO_MILK, 100 },
    { ITEM_THUNDER_STONE, 2500 },
    { ITEM_PP_UP, 1000 },
    { ITEM_FULL_RESTORE, 500 },
    { ITEM_KINGS_ROCK, 3000 },
    { ITEM_FIRE_STONE, 2500 },
    { ITEM_LEAF_STONE, 2500 },
    { ITEM_SHINY_STONE, 3000 },
    { ITEM_DUSK_STONE, 3000 },
    { 0xFFFF, 0 },
};

const struct MartItem sPokeathlonShop_NatdexFriday[] = {
    { ITEM_RED_APRICORN, 200 },
    { ITEM_YELLOW_APRICORN, 200 },
    { ITEM_GREEN_APRICORN, 200 },
    { ITEM_MOOMOO_MILK, 100 },
    { ITEM_METAL_COAT, 2500 },
    { ITEM_NUGGET, 500 },
    { ITEM_FULL_RESTORE, 500 },
    { ITEM_DRAGON_SCALE, 2500 },
    { ITEM_WATER_STONE, 2500 },
    { ITEM_SUN_STONE, 3000 },
    { ITEM_DUSK_STONE, 3000 },
    { ITEM_DAWN_STONE, 3000 },
    { 0xFFFF, 0 },
};

const struct MartItem sPokeathlonShop_NatdexSaturday[] = {
    { ITEM_GREEN_APRICORN, 200 },
    { ITEM_WHITE_APRICORN, 200 },
    { ITEM_BLACK_APRICORN, 200 },
    { ITEM_MOOMOO_MILK, 100 },
    { ITEM_LEAF_STONE, 2500 },
    { ITEM_RARE_CANDY, 2000 },
    { ITEM_FULL_RESTORE, 500 },
    { ITEM_METAL_COAT, 2500 },
    { ITEM_THUNDER_STONE, 2500 },
    { ITEM_SHINY_STONE, 3000 },
    { ITEM_DUSK_STONE, 3000 },
    { ITEM_DAWN_STONE, 3000 },
    { 0xFFFF, 0 },
};

#endif // POKEATHLON_SHOP_EXPANSION
