.include "asm/include/interop_macros.inc"

.include "asm/include/scriptmacros.inc"
.include "asm/include/flags.inc"
.include "asm/include/soundeffects.inc"
.include "asm/include/vars.inc"

.include "asm/include/events.inc"
.include "asm/include/game_stats.inc"
.include "asm/include/maps.inc"
.include "asm/include/map_sections.inc"
.include "asm/include/movements.inc"
.include "asm/include/rankings.inc"
.include "asm/include/spawns.inc"
.include "asm/include/std_scripts.inc"
.include "asm/include/trainers.inc"

#include "constants/item.h"
#include "constants/moves.h"
#include "constants/species.h"

.include "data/scr_seq/include/event_D52R0101.inc"


// text archive to grab from: 148.txt

.data


scrdef scr_seq_D52R0101_000
scrdef scr_seq_D52R0101_001
scrdef scr_seq_D52R0101_002
scrdef_end

scr_seq_D52R0101_001:
	goto_if_set FLAG_CAUGHT_GROUDON, _0040
	hasitem ITEM_RED_ORB, 1, VAR_TEMP_x4000
	compare VAR_TEMP_x4000, 1
	goto_if_ge _0072
_0040:
	setflag FLAG_HIDE_EMBEDDED_TOWER_GROUDON
	setflag FLAG_HIDE_EMBEDDED_TOWER_GROUDON_HIKER
	end

_0072:
	setflag FLAG_HIDE_EMBEDDED_TOWER_GROUDON_HIKER
	clearflag FLAG_HIDE_EMBEDDED_TOWER_GROUDON
	end

scr_seq_D52R0101_002:
	goto_if_set FLAG_ENGAGING_STATIC_POKEMON, _008B
	end

_008B:
	setflag FLAG_HIDE_EMBEDDED_TOWER_GROUDON
	hide_person obj_D52R0101_follower_mon_static_groudon
	clearflag FLAG_ENGAGING_STATIC_POKEMON
	end

scr_seq_D52R0101_000:
	play_se SEQ_SE_DP_SELECT
	lockall
	faceplayer
	play_cry SPECIES_GROUDON, 0
	npc_msg 0
	wait_cry
	closemsg
	setflag FLAG_ENGAGING_STATIC_POKEMON
	wild_battle SPECIES_GROUDON, 50, 0
	clearflag FLAG_ENGAGING_STATIC_POKEMON
	check_battle_won VAR_SPECIAL_RESULT
	compare VAR_SPECIAL_RESULT, 0
	goto_if_eq _019D
	get_static_encounter_outcome VAR_TEMP_x4002
	compare VAR_TEMP_x4002, 3
	goto_if_eq _00EC
	compare VAR_TEMP_x4002, 4
	goto_if_eq _00FB
_00EC:
	npc_msg 1
	wait_button
	closemsg
	releaseall
	end

_00FB:
	setflag FLAG_CAUGHT_GROUDON
	releaseall
	end

_019D:
	white_out
	releaseall
	end

	.balign 4
