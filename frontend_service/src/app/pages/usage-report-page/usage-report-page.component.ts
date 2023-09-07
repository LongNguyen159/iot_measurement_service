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
    const currentDate = new Date()
    const year = currentDate.getFullYear();
    const month = String(currentDate.getMonth() + 1).padStart(2, '0'); // Adding 1 to month because it's 0-based
    const day = String(currentDate.getDate()).padStart(2, '0');

    const today = `${year}-${month}-${day}`;

    // '2023-09-05'
    
    this.usageReportService.pollingResults(today).subscribe((data: Results[]) => {
      this.groupDataByDevice = groupDataByDevice(data)
      console.log('data from page:', data)
    })
  }
}
