<script type="ts">
    import Figure from "$lib/figure/Figure.svelte";
    import DataDive from "$lib/DataDive.svelte";
    import {college} from "$lib/domain/Lifestage.ts";
</script>

<DataDive
        header="Illinois CS/Computing Degree Enrollment"
        subheader="The proportion of Illinois college students enrolled into a CS/Computing degree by race/ethnicity"
>
    <svelte:fragment slot="story">
        <p>
            At the Universities in Illinois,
            Over 67 out of 100 Asian high school graduates chose CS major,
            the ratio is 15 out of 100 for white graduates,
            21 out of 100 for Hispanic students, and 13 out of 100 for black graduates.
        </p>
    </svelte:fragment>

    <svelte:fragment slot="takeaways">
        <p></p>
    </svelte:fragment>
    <Figure lifestage={college.route} name="cs_enrol" slot="figure"/>
</DataDive>

<DataDive
        header="Illinois Immediate College Enrollment Rates"
        subheader="The proportion of Illinois High School graduates that immediately enroll in college by race/ethnicity"
>
    <svelte:fragment slot="story">
        <p></p>
    </svelte:fragment>

    <svelte:fragment slot="takeaways">
        <p></p>
    </svelte:fragment>
    <Figure lifestage={college.route} name="imdEnrol" slot="figure"/>
</DataDive>