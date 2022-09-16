<script type="ts">
    import IndicatorCard from "$lib/cards/IndicatorCard.svelte";
    import Lipsum from "$lib/Lipsum.svelte";
    import AccessSnippet from "$lib/indicator-snippets/AccessSnippet.svelte";
    import ProficiencySnippet from "$lib/indicator-snippets/ProficiencySnippet.svelte";
    import ExcellenceSnippet from "$lib/indicator-snippets/ExcellenceSnippet.svelte";

    export let title: string;
</script>

<a href="access" class="md:hidden">
    <IndicatorCard>
        <AccessSnippet score="20.1"/>
    </IndicatorCard>
</a>

<a href="proficiency" class="md:hidden">
    <IndicatorCard>
        <ProficiencySnippet score="20.1"/>
    </IndicatorCard>
</a>

<IndicatorCard>
    <ExcellenceSnippet score="20.1"/>

    <svelte:fragment slot="more">
        <p>
            <Lipsum words="30"/>
        </p>
        <p>
            <Lipsum words="30"/>
        </p>
    </svelte:fragment>
</IndicatorCard>