<script type="ts">
    import Figure from "$lib/figure/Figure.svelte";
    import DataDive from "$lib/DataDive.svelte";
    import {k8} from "$lib/domain/Lifestage.ts";
</script>

<DataDive
        header="Lack of Household Internet Access"
        subheader="Percent of young residents lacking household internet access by race/ethnicity"
>
    <svelte:fragment slot="story">
        <p>
            In Chicago, almost 2 out of 10 black and Hispanic populations aged from 5 to 17 don’t have household
            internet access, in comparison with 1 out of 10 white and Asian populations don’t have household internet
            access.
        </p>
        <p>
            Overall, the younger population in Chicago has a significantly lower (11.3% to 17.3%) household Internet
            access rate in comparison with the national average across all ethnic groups
        </p>
    </svelte:fragment>
    <svelte:fragment slot="takeaways">
        <p>
            The proportion of black children and teenagers who do not have household internet access is 9 times higher
            than the national average.
        </p>
        <p>
            The proportion of Hispanic children and teenagers who do not have household internet access is 2.7 times
            higher than the national average
        </p>
    </svelte:fragment>
    <Figure lifestage={k8.route} name="noInt" slot="figure"/>
</DataDive>

<DataDive
        header="CPS K-8 STEM Magnet School Enrollment "
        subheader="Percent of CPS K-8 students enrolled in a STEM magnet school by race/ethnicity"
>
    <svelte:fragment slot="summary">
        <p>
            Asians and Black students have the highest STEM Magnet school enrollment rate relative to their population
            size in K-8. 1.8 times higher than Hispanics, and 2.8 times higher than white students
        </p>
    </svelte:fragment>
    <svelte:fragment slot="takeaways">
        <p>
            The proportion of Black students enrolled in K-8 STEM Magnet schools is twice that of Hispanic students.
        </p>
    </svelte:fragment>
    <Figure lifestage={k8.route} name="magnet_enrol" slot="figure"/>
</DataDive>

<DataDive
        header="8th grade algebra 1 enrollment"
        subheader="Percent of CPS 8th graders enrolled into algebra 1 by race/ethnicity"
>
    <svelte:fragment slot="summary">
        <p>
            The algebra enrollment rate of Asians and white students is significantly higher than that of Hispanic and
            Black students. 2.4 times higher than Hispanics, and 4.4 times higher than black.
        </p>
    </svelte:fragment>
    <svelte:fragment slot="takeaways">
        <p>
            Significant gap between H/B and W/A. The algebra 1 class enrollment rates for White and Asian in CPS are
            14-20% higher than the national average, however, that of Hispanics and Black students is 2% higher and 3%
            lower than the national average.
        </p>
        <p>
            In relation to the national average algebra enrollment rate, White and Asian students are outperforming,
            while black students are.
        </p>
    </svelte:fragment>
    <Figure lifestage={k8.route} name="algebra_enrol" slot="figure"/>
</DataDive>
