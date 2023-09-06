import { ComponentFixture, TestBed } from '@angular/core/testing';

import { UsageReportPageComponent } from './usage-report-page.component';

describe('UsageReportPageComponent', () => {
  let component: UsageReportPageComponent;
  let fixture: ComponentFixture<UsageReportPageComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [UsageReportPageComponent]
    });
    fixture = TestBed.createComponent(UsageReportPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
