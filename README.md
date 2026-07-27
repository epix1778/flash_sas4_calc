# flash_sas4_calc
Accurate flash SAS4 calculator

TO DO LIST/KNOWN ISSUES

        - my code sucks (unfixable)
        - prem guns/cs guns won't calculate if wrong rarity is selected
        - burst guns are completely wrong atm (doesn't factor in burst count/delay (will fix this eventually))
        - class skills cooldowns are not factored into average dps calc
        - need to change dropdowns back to radio buttons?
        - capacity calc probably slightly wrong for low capacity pistols w/ mastery
        - average dps slightly wrong (i don't understand alber)
        - target system needs to be finished
        - pinpoint calculated incorrectly (?)
        - move results table to right side of screen
        - add remaining features: one shots until wave x, one clips until wave x, pierce, shielder dps, finish ttk, screenshot feature?, movement penalty, range slider/visualizer?
        - bcb and mastery adaptives do not affect target ehp yet
        - class skill cooldowns are not factored into ttk calc
        - need to make it so selecting a boss target automatically assumes shooting at boss
        - add min/max ttk?
        - add wallbang option for zerf (since ttk is wrong (isn't it just 2x dps since crits are tied to each?))
        - dot unaccounted for in ttk

Version 0.1
- Initial release

Version 0.2
- Fixed files not loading
- Fixed max everything buttons
- Fixed bug with Furie rps
- Fixed bug with Trident projectile count
- Resorted guns into categories
- Fixed semi-auto fire rates
- Fixed Hornet damage (there are bound to be other damage problems)
- Removed flamer mastery

Version 0.3
- Updated results formatting greatly
- Fixed T5 shotgun mastery not contributing to calculations
- Added temporary boss target checkmark for T3 AR mastery/Zerfallen half damage

Version 0.3.1
- Added pellet count multiplier to DoT

Version 0.4
- Added TTK calc for SNEs (will add other enemies + more ttk info later)

Version 0.4.1
- Fixed Zerfallen capacity bug
