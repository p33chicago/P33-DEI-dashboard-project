<script type="ts">
    import Figure from "$lib/figure/Figure.svelte";
    import DataDive from "$lib/DataDive.svelte";
    import {college} from "$lib/domain/Lifestage.ts";
</script>

<DataDive
        header="Illinois CS/Computing Degree Persistence"
        subheader="The proportion of Illinois college students that enrolled and obtained a CS/Computing degree by race/ethnicity"
>
    <svelte:fragment slot="story">
        <p>
            At the University in Illinois, the number of students who obtain a diploma in CS is less than 1/3 of the
            total enrollment in the CS program.
        </p>
        <p>
            The number of Hispanic and Black students who obtain a diploma in CS is around 1/5 of the total enrollment
            in the CS program.
        </p>
    </svelte:fragment>

    <svelte:fragment slot="takeaways">
        <p>
            Around 1 out of 5 Black and Hispanic students at the universities of Illinois who enrolled in the CS program
            drop off.
        </p>
    </svelte:fragment>
    <Figure lifestage={college.route} name="cs_persist" slot="figure"/>
</DataDive>

<DataDive
        header="Illinois CS/Computing Degree Conferral"
        subheader="The proportion of Illinois degrees conferred that are CS/Computing degrees by race/ethnicity"
>
    <svelte:fragment slot="story">
        <p>
            At the Universities in Illinois, Over 13 out of 100 Asian graduates are CS majors, the ratio is 3 out of 100
            for other ethnic groups.
        </p>
    </svelte:fragment>

    <svelte:fragment slot="takeaways">
        <p>
            At the Universities in Illinois, the percentage of Hispanic and Black students who obtained a CS diploma is
            similar to that of White students but massively lower than Asian students.
        </p>
    </svelte:fragment>
    <Figure lifestage={college.route} name="cs_confer" slot="figure"/>
</DataDive>