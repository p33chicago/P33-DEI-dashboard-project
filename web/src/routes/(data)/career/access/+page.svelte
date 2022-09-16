<script type="ts">
    import IndicatorCard from "$lib/cards/IndicatorCard.svelte";
    import AccessSnippet from "$lib/indicator-snippets/AccessSnippet.svelte";
    import ProficiencySnippet from "$lib/indicator-snippets/ProficiencySnippet.svelte";
    import ExcellenceSnippet from "$lib/indicator-snippets/ExcellenceSnippet.svelte";
</script>

<IndicatorCard>
    <AccessSnippet score="20.1"/>

    <svelte:fragment slot="more">
        <div class="py-6">
            <h2>CPS K-8 STEM Magnet School Enrollment</h2>
            <p>The proportion of CPS K-8 students...</p>
        </div>
        <div class="grid grid-cols-2 gap-4">
            <div>
                <h3>What does the data tell?</h3>
                <p>Undead malus De horrifying poenae caro zombie,
                    implent sit ab Summus Craven Zombie undead, viscera Terror grusome max cerebro.
                    Cerebro mortuum ante? Nigh accedens, corpses infecti monstra walking ferae, A fames tremor.
                    Lumbering nostra viral mortuis Putridi for mauris sicut carne mortui creaturas in malum,
                    fascinati iam darkness burial agite shaun kingdead ferae monstra comedat.
                </p>
            </div>
            <div class="box-border h-96 w-128 p-4 border-4">GRAPH?</div>
        </div>
        <div class="py-6">
            <a class="inline-block leading-8 bg-white border-2 rounded md:px-3 lg:px-4 uppercase" href="#">help fix
                this</a>
            <a class="inline-block leading-8 bg-white border-2 rounded md:px-3 lg:px-4 uppercase" href="#">download
                data</a>
            <a class="inline-block leading-8 bg-white border-2 rounded md:px-3 lg:px-4 uppercase" href="#">share
                this</a>
        </div>
        <hr/>
        <div class="py-6">
            <h2>8th Grade Enrollment</h2>
            <p>The proportion of CPS 8th grade students...</p>
        </div>
        <div class="grid grid-cols-2 gap-4 p">
            <div>
                <h3>What does the data tell?</h3>
                <p>Undead malus De horrifying poenae caro zombie,
                    implent sit ab Summus Craven Zombie undead, viscera Terror grusome max cerebro.
                    Cerebro mortuum ante? Nigh accedens, corpses infecti monstra walking ferae, A fames tremor.
                    Lumbering nostra viral mortuis Putridi for mauris sicut carne mortui creaturas in malum,
                    fascinati iam darkness burial agite shaun kingdead ferae monstra comedat.
                </p>
            </div>
            <div class="box-border h-96 w-128 p-4 border-4">GRAPH?</div>
        </div>
        <div class="py-6">
            <a class="inline-block leading-8 bg-white border-2 rounded md:px-3 lg:px-4 uppercase" href="#">help fix
                this</a>
            <a class="inline-block leading-8 bg-white border-2 rounded md:px-3 lg:px-4 uppercase" href="#">download
                data</a>
            <a class="inline-block leading-8 bg-white border-2 rounded md:px-3 lg:px-4 uppercase" href="#">share
                this</a>
        </div>
    </svelte:fragment>
</IndicatorCard>

<a href="proficiency" class="md:hidden">
    <IndicatorCard>
        <ProficiencySnippet score="20.1"/>
    </IndicatorCard>
</a>

<a href="excellence" class="md:hidden">
    <IndicatorCard>
        <ExcellenceSnippet score="20.1"/>
    </IndicatorCard>
</a>