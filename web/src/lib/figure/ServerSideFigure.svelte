<script lang="ts">
    import type {Lifestage} from "../domain/Lifestage.ts";
    import fs from 'fs';

    export let lifestage: Lifestage['name'];
    export let name: string;

    let svg = fs.readFileSync(`static/figures/${lifestage}/${name}.svg`, 'utf-8');
    svg = svg.replace(/<svg([^>]*)height="[^"]+" /, '<svg$1')
    svg = svg.replace(/<svg([^>]*)width="[^"]+" /, '<svg$1')
</script>

<div class="overflow-scroll">
    <div class="min-w-[360px] min-h-[200px] w-full h-full">
        {@html svg}
    </div>
</div>