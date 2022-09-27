<script type="ts">
    // import Figure from "$lib/figure/Figure.svelte";
    import DataDive from "$lib/DataDive.svelte";
    // import {career} from "$lib/domain/Lifestage.ts";
</script>

<DataDive
        header="Chicago MSA TOP3 tech employee demographics"
        subheader="Chicago MSA Employee Demographics for high paying tech jobs"
>
    <svelte:fragment slot="story">
        <p>
            In the Chicago metropolitan region,
            out of 1000 Asian workers in tech occupation,
            12 of them are computer and information systems managers,
            computer network architects, or hardware engineers.
            This ratio is 7 out of 1000 for white and Hispanic workers, and 4 for black workers.
        </p>
    </svelte:fragment>

    <svelte:fragment slot="takeaways">
        <p>
            1 out of 250 black workers can land a top-paid tech job in the Chicago Metropolitan area. That rate for Hispanic workers is 1 out of 150.
        </p>
    </svelte:fragment>
    <!--    <Figure lifestage={career.route} name="techJob_topThree" slot="figure"/>-->
</DataDive>
