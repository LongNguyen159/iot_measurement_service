import { Injectable } from '@angular/core';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { Observable, map } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UsageReportService {
  apiEndpoint = 'http://localhost:8000'

  constructor(private http: HttpClient) { }

  getYearlyResults(year: number): Observable<any> {
    return this.http.get(`${this.apiEndpoint}/results/${year}?skip=0&limit=100`).pipe(
      map((data: any)=> {
        const xAxisData = data.race_names
        const seriesData = data.data.map((driver: any) => ({
          name: driver.driver,
          type: 'line',
          data: driver.points
        }))

        return {
          xAxisData,
          seriesData
        }
      })
    )
  }

  getYearList(): Observable<any> {
    return this.http.get(`${this.apiEndpoint}/years/`)
  }
}
