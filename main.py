from npc.npc import NPC 

if __name__ == "__main__":
    # Generate and print 5 NPCs
    for i, _ in enumerate(range(5), start=1):
        npc = NPC()
        print(f"{i}) {npc}")
    