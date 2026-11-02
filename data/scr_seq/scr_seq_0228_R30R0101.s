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

.include "data/scr_seq/include/event_R30R0101.inc"


// text archive to grab from: 376.txt

.data


scrdef scr_seq_R30R0101_000
scrdef scr_seq_R30R0101_001
scrdef_end

scr_seq_R30R0101_000:
	play_se SEQ_SE_DP_SELECT
	lockall
	faceplayer
	goto_if_set FLAG_GOT_APRICORN_BOX, _0041
	npc_msg 0
	giveitem_no_check ITEM_APRICORN_BOX, 1
	setflag FLAG_GOT_APRICORN_BOX
	setvar VAR_SCENE_ROUTE_30_OW, 1
	npc_msg 2
	wait_button
	closemsg
	releaseall
	end

_0041:
	npc_msg 3
	wait_button
	closemsg
	releaseall
	end

scr_seq_R30R0101_001:
	play_se SEQ_SE_DP_SELECT
	lockall
	faceplayer
	goto_if_set FLAG_GAME_CLEAR, _collector_hello
	npc_msg 4
	wait_button
	closemsg
	releaseall
	end

_collector_hello:
	npc_msg 5
	touchscreen_menu_hide
_collector_main:
	npc_msg 6
	menu_init 1, 1, 0, 1, VAR_SPECIAL_RESULT
	menu_item_add 15, 255, 0
	menu_item_add 16, 255, 1
	menu_item_add 17, 255, 2
	menu_item_add 18, 255, 3
	menu_item_add 19, 255, 4
	menu_item_add 20, 255, 5
	menu_item_add 21, 255, 6
	menu_item_add 14, 255, 7
	menu_exec
	compare VAR_SPECIAL_RESULT, 0
	goto_if_eq _collector_items
	compare VAR_SPECIAL_RESULT, 1
	goto_if_eq _collector_page_0
	compare VAR_SPECIAL_RESULT, 2
	goto_if_eq _collector_page_1
	compare VAR_SPECIAL_RESULT, 3
	goto_if_eq _collector_page_2
	compare VAR_SPECIAL_RESULT, 4
	goto_if_eq _collector_page_3
	compare VAR_SPECIAL_RESULT, 5
	goto_if_eq _collector_page_4
	compare VAR_SPECIAL_RESULT, 6
	goto_if_eq _collector_page_5
_collector_bye:
	touchscreen_menu_show
	npc_msg 11
	wait_button
	closemsg
	releaseall
	end

_collector_items:
	goto_if_set FLAG_UNK_880, _collector_items_done
	npc_msg 13
	setflag FLAG_UNK_880
	setvar VAR_UNK_4043, 0x06F2
	setvar VAR_SPECIAL_x8004, ITEM_ENIGMA_STONE
	setvar VAR_SPECIAL_x8005, 1
	callstd std_give_item_verbose
	setvar VAR_SPECIAL_x8004, ITEM_RED_ORB
	setvar VAR_SPECIAL_x8005, 1
	callstd std_give_item_verbose
	goto _collector_main

_collector_items_done:
	npc_msg 12
	goto _collector_main

_collector_page_0:
	npc_msg 7
	menu_init 1, 1, 0, 1, VAR_SPECIAL_RESULT
	menu_item_add 22, 255, 0
	menu_item_add 23, 255, 1
	menu_item_add 24, 255, 2
	menu_item_add 25, 255, 3
	menu_item_add 26, 255, 4
	menu_item_add 27, 255, 5
	menu_item_add 14, 255, 6
	menu_exec
	compare VAR_SPECIAL_RESULT, 0
	goto_if_eq _collector_bulbasaur
	compare VAR_SPECIAL_RESULT, 1
	goto_if_eq _collector_charmander
	compare VAR_SPECIAL_RESULT, 2
	goto_if_eq _collector_squirtle
	compare VAR_SPECIAL_RESULT, 3
	goto_if_eq _collector_chikorita
	compare VAR_SPECIAL_RESULT, 4
	goto_if_eq _collector_cyndaquil
	compare VAR_SPECIAL_RESULT, 5
	goto_if_eq _collector_totodile
	goto _collector_main

_collector_bulbasaur:
	goto_if_set FLAG_UNK_882, _collector_have
	get_party_count VAR_SPECIAL_x8007
	compare VAR_SPECIAL_x8007, 6
	goto_if_eq _collector_full
	setflag FLAG_UNK_882
	give_mon SPECIES_BULBASAUR, 5, 0, 0, 0, VAR_SPECIAL_RESULT
	buffer_species_name 1, SPECIES_BULBASAUR, 0, 0
	goto _collector_got

_collector_charmander:
	goto_if_set FLAG_UNK_883, _collector_have
	get_party_count VAR_SPECIAL_x8007
	compare VAR_SPECIAL_x8007, 6
	goto_if_eq _collector_full
	setflag FLAG_UNK_883
	give_mon SPECIES_CHARMANDER, 5, 0, 0, 0, VAR_SPECIAL_RESULT
	buffer_species_name 1, SPECIES_CHARMANDER, 0, 0
	goto _collector_got

_collector_squirtle:
	goto_if_set FLAG_UNK_884, _collector_have
	get_party_count VAR_SPECIAL_x8007
	compare VAR_SPECIAL_x8007, 6
	goto_if_eq _collector_full
	setflag FLAG_UNK_884
	give_mon SPECIES_SQUIRTLE, 5, 0, 0, 0, VAR_SPECIAL_RESULT
	buffer_species_name 1, SPECIES_SQUIRTLE, 0, 0
	goto _collector_got

_collector_chikorita:
	goto_if_set FLAG_UNK_885, _collector_have
	get_party_count VAR_SPECIAL_x8007
	compare VAR_SPECIAL_x8007, 6
	goto_if_eq _collector_full
	setflag FLAG_UNK_885
	give_mon SPECIES_CHIKORITA, 5, 0, 0, 0, VAR_SPECIAL_RESULT
	buffer_species_name 1, SPECIES_CHIKORITA, 0, 0
	goto _collector_got

_collector_cyndaquil:
	goto_if_set FLAG_UNK_886, _collector_have
	get_party_count VAR_SPECIAL_x8007
	compare VAR_SPECIAL_x8007, 6
	goto_if_eq _collector_full
	setflag FLAG_UNK_886
	give_mon SPECIES_CYNDAQUIL, 5, 0, 0, 0, VAR_SPECIAL_RESULT
	buffer_species_name 1, SPECIES_CYNDAQUIL, 0, 0
	goto _collector_got

_collector_totodile:
	goto_if_set FLAG_UNK_887, _collector_have
	get_party_count VAR_SPECIAL_x8007
	compare VAR_SPECIAL_x8007, 6
	goto_if_eq _collector_full
	setflag FLAG_UNK_887
	give_mon SPECIES_TOTODILE, 5, 0, 0, 0, VAR_SPECIAL_RESULT
	buffer_species_name 1, SPECIES_TOTODILE, 0, 0
	goto _collector_got

_collector_page_1:
	npc_msg 7
	menu_init 1, 1, 0, 1, VAR_SPECIAL_RESULT
	menu_item_add 28, 255, 0
	menu_item_add 29, 255, 1
	menu_item_add 30, 255, 2
	menu_item_add 31, 255, 3
	menu_item_add 32, 255, 4
	menu_item_add 33, 255, 5
	menu_item_add 14, 255, 6
	menu_exec
	compare VAR_SPECIAL_RESULT, 0
	goto_if_eq _collector_treecko
	compare VAR_SPECIAL_RESULT, 1
	goto_if_eq _collector_torchic
	compare VAR_SPECIAL_RESULT, 2
	goto_if_eq _collector_mudkip
	compare VAR_SPECIAL_RESULT, 3
	goto_if_eq _collector_turtwig
	compare VAR_SPECIAL_RESULT, 4
	goto_if_eq _collector_chimchar
	compare VAR_SPECIAL_RESULT, 5
	goto_if_eq _collector_piplup
	goto _collector_main

_collector_treecko:
	goto_if_set FLAG_UNK_888, _collector_have
	get_party_count VAR_SPECIAL_x8007
	compare VAR_SPECIAL_x8007, 6
	goto_if_eq _collector_full
	setflag FLAG_UNK_888
	give_mon SPECIES_TREECKO, 5, 0, 0, 0, VAR_SPECIAL_RESULT
	buffer_species_name 1, SPECIES_TREECKO, 0, 0
	goto _collector_got

_collector_torchic:
	goto_if_set FLAG_UNK_889, _collector_have
	get_party_count VAR_SPECIAL_x8007
	compare VAR_SPECIAL_x8007, 6
	goto_if_eq _collector_full
	setflag FLAG_UNK_889
	give_mon SPECIES_TORCHIC, 5, 0, 0, 0, VAR_SPECIAL_RESULT
	buffer_species_name 1, SPECIES_TORCHIC, 0, 0
	goto _collector_got

_collector_mudkip:
	goto_if_set FLAG_UNK_88A, _collector_have
	get_party_count VAR_SPECIAL_x8007
	compare VAR_SPECIAL_x8007, 6
	goto_if_eq _collector_full
	setflag FLAG_UNK_88A
	give_mon SPECIES_MUDKIP, 5, 0, 0, 0, VAR_SPECIAL_RESULT
	buffer_species_name 1, SPECIES_MUDKIP, 0, 0
	goto _collector_got

_collector_turtwig:
	goto_if_set FLAG_UNK_88B, _collector_have
	get_party_count VAR_SPECIAL_x8007
	compare VAR_SPECIAL_x8007, 6
	goto_if_eq _collector_full
	setflag FLAG_UNK_88B
	give_mon SPECIES_TURTWIG, 5, 0, 0, 0, VAR_SPECIAL_RESULT
	buffer_species_name 1, SPECIES_TURTWIG, 0, 0
	goto _collector_got

_collector_chimchar:
	goto_if_set FLAG_UNK_88C, _collector_have
	get_party_count VAR_SPECIAL_x8007
	compare VAR_SPECIAL_x8007, 6
	goto_if_eq _collector_full
	setflag FLAG_UNK_88C
	give_mon SPECIES_CHIMCHAR, 5, 0, 0, 0, VAR_SPECIAL_RESULT
	buffer_species_name 1, SPECIES_CHIMCHAR, 0, 0
	goto _collector_got

_collector_piplup:
	goto_if_set FLAG_UNK_88D, _collector_have
	get_party_count VAR_SPECIAL_x8007
	compare VAR_SPECIAL_x8007, 6
	goto_if_eq _collector_full
	setflag FLAG_UNK_88D
	give_mon SPECIES_PIPLUP, 5, 0, 0, 0, VAR_SPECIAL_RESULT
	buffer_species_name 1, SPECIES_PIPLUP, 0, 0
	goto _collector_got

_collector_page_2:
	npc_msg 7
	menu_init 1, 1, 0, 1, VAR_SPECIAL_RESULT
	menu_item_add 34, 255, 0
	menu_item_add 35, 255, 1
	menu_item_add 36, 255, 2
	menu_item_add 37, 255, 3
	menu_item_add 38, 255, 4
	menu_item_add 39, 255, 5
	menu_item_add 40, 255, 6
	menu_item_add 14, 255, 7
	menu_exec
	compare VAR_SPECIAL_RESULT, 0
	goto_if_eq _collector_omanyte
	compare VAR_SPECIAL_RESULT, 1
	goto_if_eq _collector_kabuto
	compare VAR_SPECIAL_RESULT, 2
	goto_if_eq _collector_aerodactyl
	compare VAR_SPECIAL_RESULT, 3
	goto_if_eq _collector_lileep
	compare VAR_SPECIAL_RESULT, 4
	goto_if_eq _collector_anorith
	compare VAR_SPECIAL_RESULT, 5
	goto_if_eq _collector_cranidos
	compare VAR_SPECIAL_RESULT, 6
	goto_if_eq _collector_shieldon
	goto _collector_main

_collector_omanyte:
	goto_if_set FLAG_UNK_88E, _collector_have
	get_party_count VAR_SPECIAL_x8007
	compare VAR_SPECIAL_x8007, 6
	goto_if_eq _collector_full
	setflag FLAG_UNK_88E
	give_mon SPECIES_OMANYTE, 20, 0, 0, 0, VAR_SPECIAL_RESULT
	buffer_species_name 1, SPECIES_OMANYTE, 0, 0
	goto _collector_got

_collector_kabuto:
	goto_if_set FLAG_UNK_88F, _collector_have
	get_party_count VAR_SPECIAL_x8007
	compare VAR_SPECIAL_x8007, 6
	goto_if_eq _collector_full
	setflag FLAG_UNK_88F
	give_mon SPECIES_KABUTO, 20, 0, 0, 0, VAR_SPECIAL_RESULT
	buffer_species_name 1, SPECIES_KABUTO, 0, 0
	goto _collector_got

_collector_aerodactyl:
	goto_if_set FLAG_UNK_890, _collector_have
	get_party_count VAR_SPECIAL_x8007
	compare VAR_SPECIAL_x8007, 6
	goto_if_eq _collector_full
	setflag FLAG_UNK_890
	give_mon SPECIES_AERODACTYL, 20, 0, 0, 0, VAR_SPECIAL_RESULT
	buffer_species_name 1, SPECIES_AERODACTYL, 0, 0
	goto _collector_got

_collector_lileep:
	goto_if_set FLAG_UNK_891, _collector_have
	get_party_count VAR_SPECIAL_x8007
	compare VAR_SPECIAL_x8007, 6
	goto_if_eq _collector_full
	setflag FLAG_UNK_891
	give_mon SPECIES_LILEEP, 20, 0, 0, 0, VAR_SPECIAL_RESULT
	buffer_species_name 1, SPECIES_LILEEP, 0, 0
	goto _collector_got

_collector_anorith:
	goto_if_set FLAG_UNK_892, _collector_have
	get_party_count VAR_SPECIAL_x8007
	compare VAR_SPECIAL_x8007, 6
	goto_if_eq _collector_full
	setflag FLAG_UNK_892
	give_mon SPECIES_ANORITH, 20, 0, 0, 0, VAR_SPECIAL_RESULT
	buffer_species_name 1, SPECIES_ANORITH, 0, 0
	goto _collector_got

_collector_cranidos:
	goto_if_set FLAG_UNK_893, _collector_have
	get_party_count VAR_SPECIAL_x8007
	compare VAR_SPECIAL_x8007, 6
	goto_if_eq _collector_full
	setflag FLAG_UNK_893
	give_mon SPECIES_CRANIDOS, 20, 0, 0, 0, VAR_SPECIAL_RESULT
	buffer_species_name 1, SPECIES_CRANIDOS, 0, 0
	goto _collector_got

_collector_shieldon:
	goto_if_set FLAG_UNK_894, _collector_have
	get_party_count VAR_SPECIAL_x8007
	compare VAR_SPECIAL_x8007, 6
	goto_if_eq _collector_full
	setflag FLAG_UNK_894
	give_mon SPECIES_SHIELDON, 20, 0, 0, 0, VAR_SPECIAL_RESULT
	buffer_species_name 1, SPECIES_SHIELDON, 0, 0
	goto _collector_got

_collector_page_3:
	npc_msg 7
	menu_init 1, 1, 0, 1, VAR_SPECIAL_RESULT
	menu_item_add 41, 255, 0
	menu_item_add 42, 255, 1
	menu_item_add 43, 255, 2
	menu_item_add 44, 255, 3
	menu_item_add 45, 255, 4
	menu_item_add 46, 255, 5
	menu_item_add 47, 255, 6
	menu_item_add 14, 255, 7
	menu_exec
	compare VAR_SPECIAL_RESULT, 0
	goto_if_eq _collector_castform
	compare VAR_SPECIAL_RESULT, 1
	goto_if_eq _collector_spiritomb
	compare VAR_SPECIAL_RESULT, 2
	goto_if_eq _collector_rotom
	compare VAR_SPECIAL_RESULT, 3
	goto_if_eq _collector_uxie
	compare VAR_SPECIAL_RESULT, 4
	goto_if_eq _collector_mesprit
	compare VAR_SPECIAL_RESULT, 5
	goto_if_eq _collector_azelf
	compare VAR_SPECIAL_RESULT, 6
	goto_if_eq _collector_manaphy
	goto _collector_main

_collector_castform:
	goto_if_set FLAG_UNK_895, _collector_have
	get_party_count VAR_SPECIAL_x8007
	compare VAR_SPECIAL_x8007, 6
	goto_if_eq _collector_full
	setflag FLAG_UNK_895
	give_mon SPECIES_CASTFORM, 30, 0, 0, 0, VAR_SPECIAL_RESULT
	buffer_species_name 1, SPECIES_CASTFORM, 0, 0
	goto _collector_got

_collector_spiritomb:
	goto_if_set FLAG_UNK_896, _collector_have
	get_party_count VAR_SPECIAL_x8007
	compare VAR_SPECIAL_x8007, 6
	goto_if_eq _collector_full
	setflag FLAG_UNK_896
	give_mon SPECIES_SPIRITOMB, 30, 0, 0, 0, VAR_SPECIAL_RESULT
	buffer_species_name 1, SPECIES_SPIRITOMB, 0, 0
	goto _collector_got

_collector_rotom:
	goto_if_set FLAG_UNK_897, _collector_have
	get_party_count VAR_SPECIAL_x8007
	compare VAR_SPECIAL_x8007, 6
	goto_if_eq _collector_full
	setflag FLAG_UNK_897
	give_mon SPECIES_ROTOM, 30, 0, 0, 0, VAR_SPECIAL_RESULT
	buffer_species_name 1, SPECIES_ROTOM, 0, 0
	goto _collector_got

_collector_uxie:
	goto_if_set FLAG_UNK_898, _collector_have
	get_party_count VAR_SPECIAL_x8007
	compare VAR_SPECIAL_x8007, 6
	goto_if_eq _collector_full
	setflag FLAG_UNK_898
	give_mon SPECIES_UXIE, 50, 0, 0, 0, VAR_SPECIAL_RESULT
	buffer_species_name 1, SPECIES_UXIE, 0, 0
	goto _collector_got

_collector_mesprit:
	goto_if_set FLAG_UNK_899, _collector_have
	get_party_count VAR_SPECIAL_x8007
	compare VAR_SPECIAL_x8007, 6
	goto_if_eq _collector_full
	setflag FLAG_UNK_899
	give_mon SPECIES_MESPRIT, 50, 0, 0, 0, VAR_SPECIAL_RESULT
	buffer_species_name 1, SPECIES_MESPRIT, 0, 0
	goto _collector_got

_collector_azelf:
	goto_if_set FLAG_UNK_89A, _collector_have
	get_party_count VAR_SPECIAL_x8007
	compare VAR_SPECIAL_x8007, 6
	goto_if_eq _collector_full
	setflag FLAG_UNK_89A
	give_mon SPECIES_AZELF, 50, 0, 0, 0, VAR_SPECIAL_RESULT
	buffer_species_name 1, SPECIES_AZELF, 0, 0
	goto _collector_got

_collector_manaphy:
	goto_if_set FLAG_UNK_89B, _collector_have
	get_party_count VAR_SPECIAL_x8007
	compare VAR_SPECIAL_x8007, 6
	goto_if_eq _collector_full
	setflag FLAG_UNK_89B
	give_mon SPECIES_MANAPHY, 50, 0, 0, 0, VAR_SPECIAL_RESULT
	SetLastMonFateful
	buffer_species_name 1, SPECIES_MANAPHY, 0, 0
	goto _collector_got

_collector_page_4:
	npc_msg 7
	menu_init 1, 1, 0, 1, VAR_SPECIAL_RESULT
	menu_item_add 48, 255, 0
	menu_item_add 49, 255, 1
	menu_item_add 50, 255, 2
	menu_item_add 51, 255, 3
	menu_item_add 52, 255, 4
	menu_item_add 53, 255, 5
	menu_item_add 14, 255, 6
	menu_exec
	compare VAR_SPECIAL_RESULT, 0
	goto_if_eq _collector_regirock
	compare VAR_SPECIAL_RESULT, 1
	goto_if_eq _collector_regice
	compare VAR_SPECIAL_RESULT, 2
	goto_if_eq _collector_registeel
	compare VAR_SPECIAL_RESULT, 3
	goto_if_eq _collector_regigigas
	compare VAR_SPECIAL_RESULT, 4
	goto_if_eq _collector_heatran
	compare VAR_SPECIAL_RESULT, 5
	goto_if_eq _collector_cresselia
	goto _collector_main

_collector_regirock:
	goto_if_set FLAG_UNK_89C, _collector_have
	get_party_count VAR_SPECIAL_x8007
	compare VAR_SPECIAL_x8007, 6
	goto_if_eq _collector_full
	setflag FLAG_UNK_89C
	give_mon SPECIES_REGIROCK, 50, 0, 0, 0, VAR_SPECIAL_RESULT
	buffer_species_name 1, SPECIES_REGIROCK, 0, 0
	goto _collector_got

_collector_regice:
	goto_if_set FLAG_UNK_89D, _collector_have
	get_party_count VAR_SPECIAL_x8007
	compare VAR_SPECIAL_x8007, 6
	goto_if_eq _collector_full
	setflag FLAG_UNK_89D
	give_mon SPECIES_REGICE, 50, 0, 0, 0, VAR_SPECIAL_RESULT
	buffer_species_name 1, SPECIES_REGICE, 0, 0
	goto _collector_got

_collector_registeel:
	goto_if_set FLAG_UNK_89E, _collector_have
	get_party_count VAR_SPECIAL_x8007
	compare VAR_SPECIAL_x8007, 6
	goto_if_eq _collector_full
	setflag FLAG_UNK_89E
	give_mon SPECIES_REGISTEEL, 50, 0, 0, 0, VAR_SPECIAL_RESULT
	buffer_species_name 1, SPECIES_REGISTEEL, 0, 0
	goto _collector_got

_collector_regigigas:
	goto_if_set FLAG_UNK_89F, _collector_have
	get_party_count VAR_SPECIAL_x8007
	compare VAR_SPECIAL_x8007, 6
	goto_if_eq _collector_full
	setflag FLAG_UNK_89F
	give_mon SPECIES_REGIGIGAS, 50, 0, 0, 0, VAR_SPECIAL_RESULT
	buffer_species_name 1, SPECIES_REGIGIGAS, 0, 0
	goto _collector_got

_collector_heatran:
	goto_if_set FLAG_UNK_8A0, _collector_have
	get_party_count VAR_SPECIAL_x8007
	compare VAR_SPECIAL_x8007, 6
	goto_if_eq _collector_full
	setflag FLAG_UNK_8A0
	give_mon SPECIES_HEATRAN, 50, 0, 0, 0, VAR_SPECIAL_RESULT
	buffer_species_name 1, SPECIES_HEATRAN, 0, 0
	goto _collector_got

_collector_cresselia:
	goto_if_set FLAG_UNK_8A1, _collector_have
	get_party_count VAR_SPECIAL_x8007
	compare VAR_SPECIAL_x8007, 6
	goto_if_eq _collector_full
	setflag FLAG_UNK_8A1
	give_mon SPECIES_CRESSELIA, 50, 0, 0, 0, VAR_SPECIAL_RESULT
	buffer_species_name 1, SPECIES_CRESSELIA, 0, 0
	goto _collector_got

_collector_page_5:
	npc_msg 7
	menu_init 1, 1, 0, 1, VAR_SPECIAL_RESULT
	menu_item_add 54, 255, 0
	menu_item_add 55, 255, 1
	menu_item_add 56, 255, 2
	menu_item_add 57, 255, 3
	menu_item_add 58, 255, 4
	menu_item_add 59, 255, 5
	menu_item_add 60, 255, 6
	menu_item_add 14, 255, 7
	menu_exec
	compare VAR_SPECIAL_RESULT, 0
	goto_if_eq _collector_mew
	compare VAR_SPECIAL_RESULT, 1
	goto_if_eq _collector_celebi
	compare VAR_SPECIAL_RESULT, 2
	goto_if_eq _collector_jirachi
	compare VAR_SPECIAL_RESULT, 3
	goto_if_eq _collector_deoxys
	compare VAR_SPECIAL_RESULT, 4
	goto_if_eq _collector_darkrai
	compare VAR_SPECIAL_RESULT, 5
	goto_if_eq _collector_shaymin
	compare VAR_SPECIAL_RESULT, 6
	goto_if_eq _collector_arceus
	goto _collector_main

_collector_mew:
	goto_if_set FLAG_UNK_8A2, _collector_have
	get_party_count VAR_SPECIAL_x8007
	compare VAR_SPECIAL_x8007, 6
	goto_if_eq _collector_full
	setflag FLAG_UNK_8A2
	give_mon SPECIES_MEW, 50, 0, 0, 0, VAR_SPECIAL_RESULT
	SetLastMonFateful
	buffer_species_name 1, SPECIES_MEW, 0, 0
	goto _collector_got

_collector_celebi:
	goto_if_set FLAG_UNK_8A3, _collector_have
	get_party_count VAR_SPECIAL_x8007
	compare VAR_SPECIAL_x8007, 6
	goto_if_eq _collector_full
	setflag FLAG_UNK_8A3
	give_mon SPECIES_CELEBI, 50, 0, 0, 0, VAR_SPECIAL_RESULT
	SetLastMonFateful
	buffer_species_name 1, SPECIES_CELEBI, 0, 0
	goto _collector_got

_collector_jirachi:
	goto_if_set FLAG_UNK_8A4, _collector_have
	get_party_count VAR_SPECIAL_x8007
	compare VAR_SPECIAL_x8007, 6
	goto_if_eq _collector_full
	setflag FLAG_UNK_8A4
	give_mon SPECIES_JIRACHI, 50, 0, 0, 0, VAR_SPECIAL_RESULT
	SetLastMonFateful
	buffer_species_name 1, SPECIES_JIRACHI, 0, 0
	goto _collector_got

_collector_deoxys:
	goto_if_set FLAG_UNK_8A5, _collector_have
	get_party_count VAR_SPECIAL_x8007
	compare VAR_SPECIAL_x8007, 6
	goto_if_eq _collector_full
	setflag FLAG_UNK_8A5
	give_mon SPECIES_DEOXYS, 50, 0, 0, 0, VAR_SPECIAL_RESULT
	SetLastMonFateful
	buffer_species_name 1, SPECIES_DEOXYS, 0, 0
	goto _collector_got

_collector_darkrai:
	goto_if_set FLAG_UNK_8A6, _collector_have
	get_party_count VAR_SPECIAL_x8007
	compare VAR_SPECIAL_x8007, 6
	goto_if_eq _collector_full
	setflag FLAG_UNK_8A6
	give_mon SPECIES_DARKRAI, 50, 0, 0, 0, VAR_SPECIAL_RESULT
	SetLastMonFateful
	buffer_species_name 1, SPECIES_DARKRAI, 0, 0
	goto _collector_got

_collector_shaymin:
	goto_if_set FLAG_UNK_8A7, _collector_have
	get_party_count VAR_SPECIAL_x8007
	compare VAR_SPECIAL_x8007, 6
	goto_if_eq _collector_full
	setflag FLAG_UNK_8A7
	give_mon SPECIES_SHAYMIN, 50, 0, 0, 0, VAR_SPECIAL_RESULT
	SetLastMonFateful
	buffer_species_name 1, SPECIES_SHAYMIN, 0, 0
	goto _collector_got

_collector_arceus:
	goto_if_set FLAG_UNK_8A8, _collector_have
	get_party_count VAR_SPECIAL_x8007
	compare VAR_SPECIAL_x8007, 6
	goto_if_eq _collector_full
	setflag FLAG_UNK_8A8
	give_mon SPECIES_ARCEUS, 50, 0, 0, 0, VAR_SPECIAL_RESULT
	SetLastMonFateful
	buffer_species_name 1, SPECIES_ARCEUS, 0, 0
	goto _collector_got

_collector_got:
	buffer_players_name 0
	npc_msg 10
	play_fanfare SEQ_ME_POKEGET
	wait_fanfare
	goto _collector_main

_collector_have:
	npc_msg 8
	goto _collector_main

_collector_full:
	npc_msg 9
	goto _collector_main
	.balign 4
