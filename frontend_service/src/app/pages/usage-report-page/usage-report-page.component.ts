import { Component, OnInit } from '@angular/core';
import { UsageReportService } from '../../feature/usage-report/services/usage-report.service';

import { groupDataByDevice } from 'src/app/feature/utils/data-process';
import { Results } from 'src/app/feature/usage-report/models/results';

@Component({
  selector: 'app-usage-report-page',
  templateUrl: './usage-report-page.component.html',
  styleUrls: ['./usage-report-page.component.scss']
})
export class UsageReportPageComponent implements OnInit {
  groupDataByDevice: any
  

  constructor(private usageReportService: UsageReportService) {}

  ngOnInit(): void {
    this.usageReportService.getDailyResults('2023-09-05').subscribe((data: Results[]) => {
      this.groupDataByDevice = groupDataByDevice(data)
    })
  }
}
