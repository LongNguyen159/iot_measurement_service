import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LinePlotComponent } from './line-plot.component';

describe('LinePlotComponent', () => {
  let component: LinePlotComponent;
  let fixture: ComponentFixture<LinePlotComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [LinePlotComponent]
    });
    fixture = TestBed.createComponent(LinePlotComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
