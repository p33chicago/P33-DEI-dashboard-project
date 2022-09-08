<script>
    import DataSidebar from "$lib/DataSidebar.svelte";
    import LifestageTitleCard from "$lib/LifestageTitleCard.svelte";
    import LifestageIndexCard from "$lib/LifestageIndexCard.svelte";
    import LifestageIndicatorsCard from "$lib/LifestageIndicatorsCard.svelte";
</script>

<DataSidebar>
    <LifestageTitleCard slot="title" title="College" />
    <LifestageIndexCard slot="index" chicago="40" us="70" />
    <LifestageIndicatorsCard slot="indicators" access="10" excellence="1" proficiency="2" />
</DataSidebar>

<slot />