import { Component, OnInit } from '@angular/core';
import { ModalService } from '../../_modal/modal.service';
import { NgForm } from '@angular/forms';
import { TestService } from '../../test.service';
import { Observable } from 'rxjs';

@Component({
  selector: 'bug-report',
  templateUrl: './bug-report.component.html',
  styleUrls: ['./bug-report.component.css']
})
export class BugReportComponent implements OnInit {
  button: string = 'Сообщить об ошибке';

  email: string = '';
  message: string = '';

  constructor(private modalService: ModalService, private testService: TestService) {
  }

  public onSubmit(email: string, message: string) {
    //this.testService.onSubmit(email, message);
    this.testService.sendBugReport(email, message);
    this.closeModal('bug-report');
  }

  openModal(id: string) {
    this.modalService.open(id);
  }
  
  closeModal(id: string) {
    this.modalService.close(id);
  }

  ngOnInit(): void {
  }

}
