<script lang="ts">
    import type {Lifestage} from "../domain/Lifestage.ts";
    import fs from 'fs';

    export let lifestage: Lifestage['name'];
    export let name: string;

    let svg = fs.readFileSync(`static/figures/${lifestage}/${name}.svg`, 'utf-8');
</script>

<svg>{@html svg}</svg>

<style>
    svg {
        width: 100%;
        aspect-ratio: 1/1;
    }
</style>