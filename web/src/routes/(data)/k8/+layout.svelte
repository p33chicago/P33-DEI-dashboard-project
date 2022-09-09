<script>
    import DataSidebar from "$lib/DataSidebar.svelte";
    import LifestageTitleCard from "$lib/LifestageTitleCard.svelte";
    import LifestageIndexCard from "$lib/LifestageIndexCard.svelte";
    import LifestageIndicatorsCard from "$lib/LifestageIndicatorsCard.svelte";
import DataMain from "$lib/DataMain.svelte";
import SummaryCard from "$lib/SummaryCard.svelte";
</script>

<div class="flex">
    <DataSidebar>
        <LifestageTitleCard slot="title" title="K-8" />
        <LifestageIndexCard slot="index" chicago="40" us="70" />
        <LifestageIndicatorsCard slot="indicators" access="10" excellence="1" proficiency="2" />
    </DataSidebar>
    <DataMain>
        <SummaryCard slot="title" title="Methodology" />
    </DataMain>
    <slot />
</div>
