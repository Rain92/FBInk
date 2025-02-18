#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#
# Quick'n dirty script to generate the Kobo PCB to Product LUT
# c.f., /bin/kobo_config.sh
#
##

data = "./Kobo_PCB_IDs.txt"

with open(data, "r") as f:
	for line in f:
		# NOTE: Start with the Tolinos, as we have a complete PCB ID for them,
		#       c.f., https://github.com/NiLuJe/FBInk/issues/70#issuecomment-1242274710
		if line.startswith("E60QF0"):
			# Tolino Shine 2HD
			print("32627,")
#		elif line.startswith("E60K00"):
#			# NOTE: Caught by the Clara HD match
#			# Tolino Shine 3
#			print("32632,")
		elif line.startswith("E70K0M"):
			# NOTE: Its actual DTB says E70K0M, but at the same index as E70K00, which is the Libra...
			# Tolino Vision 5
			print("32640,")
		elif line.startswith("E60610D"):
			# NOTE: This is an educated guess. kobo_config puts every E60610* in the "trilogy" basket...
			# Touch C (trilogy) [320]
			print("320,")
		elif line.startswith("E60610"):
			# Touch A/B (trilogy) [310]
			print("310,")
		elif line.startswith("E60QB") or line.startswith("E606B"):
			# Glo (kraken) [330]
			print("330,")
		elif line.startswith("E5061"):
			# Mini (pixie) [340]
			print("340,")
		elif line.startswith("E60Q9"):
			# Touch 2.0 (pika) [372] (if 800x600)
			# Glo HD (alyssum) [371] (if !800x600)
			print("371,")
		elif line.startswith("E606C"):
			# Aura HD (dragon) [350]
			print("350,")
		elif line.startswith("E606G"):
			# Aura H2O (dahlia) [370]
			print("370,")
		elif line.startswith("E606F"):
			# Aura (phoenix) [360]
			print("360,")
		elif line.startswith("E70Q0"):
			# Aura ONE (daylight) [373]
			# Aura ONE LE (daylight) [381] (if 32GB)
			print("373,")
		elif line.startswith("E60K0") or line.startswith("E60U1"):
			# Clara HD (nova) [376]
			print("376,")
		elif line.startswith("E60QL") or line.startswith("E60U0") or line.startswith("T60Q0"):
			# Aura SE (star) [375]
			# Aura SE r2 (star) [379] (if mx6sll)
			print("375,")
		elif line.startswith("E60QM"):
			# Aura H2O² (snow) [374]
			# Aura H2O² r2 (snow) [378] (if mx6sll)
			print("374,")
		elif line.startswith("E80K0"):
			# Forma (frost) [377]
			# Forma 32GB (frost) [380] (if 32GB)
			print("377,")
		elif line.startswith("E70K0"):
			# Libra (storm) [384]
			print("384,")
		elif line.startswith("E60U2"):
			# Nia (luna) [382]
			print("382,")
		elif line.startswith("EA0P1"):
			# Elipsa (europa) [387]
			print("387,")
		elif line.startswith("E70K1"):
			# Libra 2 (io) [388]
			print("388,")
		elif line.startswith("E80P0"):
			# Sage (cadmus) [383]
			print("383,")
		elif line.startswith("E60K2"):
			# Clara 2E (goldfinch) [386]
			print("386,")
		else:
			print("0,")
