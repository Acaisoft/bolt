/**
 * Copyright (c) 2022 Acaisoft
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy of
 * this software and associated documentation files (the "Software"), to deal in
 * the Software without restriction, including without limitation the rights to
 * use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
 * the Software, and to permit persons to whom the Software is furnished to do so,
 * subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
 * FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
 * COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
 * IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
 * CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 */

import React from 'react'
import moment from 'moment'
import { SectionHeader, DataTable, Button } from 'components'
import { useQuery } from '@apollo/client'
import { Typography } from '@material-ui/core'
import { useParams } from 'react-router-dom'
import { GET_SCENARIO } from './graphql'
import useStyles from './ScenarioDetails.styles'

const TestScenarioDetails = () => {
  const params = useParams()
  const { scenarioId } = params
  const classes = useStyles()
  const { loading, data: { externalTestScenario = [] } = {} } = useQuery(
    GET_SCENARIO,
    {
      variables: { scenarioId },
      fetchPolicy: 'cache-and-network',
    }
  )

  return (
    <React.Fragment>
      <SectionHeader
        title={externalTestScenario.name || ''}
        description="E2E Scenario"
      ></SectionHeader>
      <Typography
        color="textSecondary"
        component="p"
        variant="body1"
        className={classes.marginTop}
      >
        {externalTestScenario.description || ''}
      </Typography>
      <div className={classes.marginTop}>
        <DataTable
          data={externalTestScenario.test_runs}
          isLoading={loading}
          rowKey={test_run => test_run.id}
        >
          <DataTable.Column
            render={test_run =>
              moment(test_run.timestamp).format('YYYY-MM-DD HH:mm:ss')
            }
            title="Run Date"
          />
          <DataTable.Column
            render={test_run => (
              <div className={classes.success}>
                {test_run.total -
                  (test_run.failures + test_run.errors + test_run.skipped)}
              </div>
            )}
            title="Successes"
          />
          <DataTable.Column render={test_run => test_run.skipped} title="Skipped" />
          <DataTable.Column
            render={test_run => (
              <div className={classes.failure}>{test_run.failures}</div>
            )}
            title="Failures"
          />
          <DataTable.Column render={test_run => test_run.total} title="Total" />
          <DataTable.Column
            key="actions"
            render={scenario => {
              return (
                <div className={classes.actionsContainer}>
                  <Button
                    data-testid={`scenario-${scenario.id}-details`}
                    // href={getE2ETestRunsListUrl({
                    //   id: scenario.id,
                    // })}
                    title="Show scenario details"
                    variant="link"
                  >
                    Details
                  </Button>
                </div>
              )
            }}
            title="Actions"
          />
        </DataTable>
      </div>
    </React.Fragment>
  )
}

export default TestScenarioDetails