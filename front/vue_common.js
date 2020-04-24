Vue.prototype.$http = axios

new Vue({
  el: '#search',
  data() {
    return {
          region_selected: true,
          case_selected: true,
          number_selected: true,
          r_response: false,
          serverError: false,
          serverErrorInfo: null,
          data: null,
          form_default: {
              region: "",
              r_case: "",
              benefit: "",
              r_number: "",
              r_location: "",
          },
          regions: [
            { text: 'dolnośląskie', value: '01' },
            { text: 'kujawsko-pomorskie', value: '02' },
            { text: 'lubelskie', value: '03' },
            { text: 'lubuskie', value: '04' },
            { text: 'łódzkie', value: '05' },
            { text: 'małopolskie', value: '06' },
            { text: 'mazowieckie', value: '07' },
            { text: 'opolskie', value: '08' },
            { text: 'podkarpackie', value: '09' },
            { text: 'podlaskie', value: '10' },
            { text: 'pomorskie', value: '11' },
            { text: 'śląskie', value: '12' },
            { text: 'świętokrzyskie', value: '13' },
            { text: 'warmińsko-mazurskie', value: '14' },
            { text: 'wielkopolskie', value: '15' },
            { text: 'zachodniopomorskie', value: '16' }
          ],
          r_cases: [
            { text: 'stabilny', value: '1'},
            { text: 'pilny', value: '2'},
          ],
          numbers: [
            { text: '11', value: '11'},
            { text: '12', value: '12'},
            { text: '13', value: '13'},
            { text: '14', value: '14'},
            { text: '15', value: '15'},
            { text: '16', value: '16'},
            { text: '17', value: '17'},
            { text: '18', value: '18'},
            { text: '19', value: '19'},
            { text: '20', value: '20'},
            { text: '21', value: '21'},
            { text: '22', value: '22'},
            { text: '23', value: '23'},
            { text: '24', value: '24'},
            { text: '25', value: '25'},
          ],
    }
  },
  methods: {
      applyInputStyle: function(isSelected) {
          return [isSelected ? 'good-input-ok' : 'no-input-warning'];
      },
      posts: function() {
          // first validate data
          var good = true
          if (!this.form_default.region) {
              console.log("no region");
              good = false;
              this.region_selected = false;
          } else {
              this.region_selected = true;
          }
          if (!this.form_default.r_case) {
              console.log("no case");
              good = false;
              this.case_selected = false;
          } else {
              this.case_selected = true;
          }
          if (!this.form_default.r_number) {
              console.log("no number");
              good = false;
              this.number_selected = false;
          } else {
              this.number_selected = true;
          }
          if(!good) {
              // missing form fields
              return;
          }
          // debug - print selected fields
          console.log("region " + this.form_default.region);
          console.log("case " + this.form_default.r_case);
          console.log("benefit " + this.form_default.benefit);
          var self=this;
     
          this.$http.get('http://localhost:8080/get', {
              params: {
                r_region: this.form_default.region,
                r_case: this.form_default.r_case,
                r_benefit: this.form_default.benefit,
                r_number: this.form_default.r_number,
                r_location: this.form_default.r_location
              }
          }).then(function(response){
            if(response.status == "200"){
              self.data = response.data;
              self.r_response = true;
              self.serverError = false;
              // console.log(this.r_response);
          }
      
        }).catch((e) => {
            console.log(e);
            self.serverErrorInfo = e;
            self.serverError = true;
        }
      )
    }
  }
})
