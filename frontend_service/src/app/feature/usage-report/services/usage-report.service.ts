import { Injectable } from '@angular/core';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { Observable, map, interval, startWith, mergeMap } from 'rxjs';
import { Results } from '../models/results';

@Injectable({
  providedIn: 'root'
})
export class UsageReportService {
  apiEndpoint = 'http://localhost:8000'
  pollingInterval = 5000;

  constructor(private http: HttpClient) { }

  getDailyResults(date: string): Observable<Results[]> {
    return this.http.get<any[]>(`${this.apiEndpoint}/daily-results?target_date=${date}`)
      .pipe(
        map(data => this.mapData(data)) // Use the map operator to map data
      );
  }

  private mapData(data: any[]): Results[] {
    // Map JSON data to Results interface
    return data.map(item => ({
      id: item.ID,
      deviceId: item.DeviceID,
      timestamp: item.Timestamp,
      temperature: item.Temperature
    }));
  }

  pollingResults(date: string): Observable<Results[]> {
    return interval(this.pollingInterval).pipe(
      startWith(0),
      mergeMap(() => this.getDailyResults(date))
    )
  }

  // getYearlyResults(year: number): Observable<any> {
  //   return this.http.get(`${this.apiEndpoint}/results/${year}?skip=0&limit=100`).pipe(
  //     map((data: any)=> {
  //       const xAxisData = data.race_names
  //       const seriesData = data.data.map((driver: any) => ({
  //         name: driver.driver,
  //         type: 'line',
  //         data: driver.points
  //       }))

  //       return {
  //         xAxisData,
  //         seriesData
  //       }
  //     })
  //   )
  // }

  // getYearList(): Observable<any> {
  //   return this.http.get(`${this.apiEndpoint}/years/`)
  // }
}
