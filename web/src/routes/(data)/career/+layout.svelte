<script>
    import DataSidebar from "$lib/DataSidebar.svelte";
    import LifestageTitleCard from "$lib/LifestageTitleCard.svelte";
    import LifestageIndexCard from "$lib/LifestageIndexCard.svelte";
    import LifestageIndicatorsCard from "$lib/LifestageIndicatorsCard.svelte";
</script>

<DataSidebar>
    <LifestageTitleCard slot="title" title="K-8" />
    <LifestageIndexCard slot="index" chicago="40" us="70" />
    <LifestageIndicatorsCard slot="indicators" access="10" excellence="1" proficiency="2" />
</DataSidebar>
<div class="col-span-4 md:col-span-3 space-y-6">
    <slot />
</div>
