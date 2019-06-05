<template>
<div>
  <b-card bg-variant="light">
    <b-form-group
      @submit="onSubmit"
      label-cols-lg="3"
      label="Adopt Dog Post"
      label-size="lg"
      label-class="font-weight-bold pt-0"
      class="mb-0"
    >
      <b-form-group
        label-cols-sm="3"
        label="Title:"
        label-align-sm="right"
        label-for="nested-title"
      >
        <b-form-input id="nested-title" v-model="title"></b-form-input>
      </b-form-group>

      <b-form-group
        label-cols-sm="3"
        label="Phone number:"
        label-align-sm="right"
        label-for="nested-phone-number"
      >
        <b-form-input id="nested-phone-number" v-model="phone_num"></b-form-input>
      </b-form-group>

      <b-form-group
        label-cols-sm="3"
        label="Dog Type:"
        label-align-sm="right"
        label-for="nested-dog-type"
      >
        <b-form-input id="nested-dog-type" v-model="dog_type"></b-form-input>
      </b-form-group>

      <b-form-group
        label-cols-sm="3"
        label="Dog age:"
        label-align-sm="right"
        label-for="nested-dog-age"
      >
        <b-form-input id="nested-dog-age" v-model="dog_age"></b-form-input>
      </b-form-group>

      <b-form-group
        label-cols-sm="3"
        label="Dog sex:"
        label-align-sm="right"
        label-for="nested-dog-sex"
      >
        <b-form-radio-group
          id="dog-sex"
          v-model="dog_sex"
          class="pt-2"
          :options="['Male', 'Female']"
        ></b-form-radio-group>
      </b-form-group>

      <b-form-group
        label-cols-sm="3"
        label="Neutralizer:"
        label-align-sm="right"
        label-for="nested-neutralizer"
      >
        <b-form-radio-group
          id="nested-neutralizer"
          v-model="is_neu"
          class="pt-2"
          :options="['Yes', 'No']"
        ></b-form-radio-group>
      </b-form-group>

      <b-form-group
        label-cols-sm="3"
        label="Vaccine:"
        label-align-sm="right"
        label-for="nested-vaccine"
      >
        <b-form-radio-group
          id="nested-vaccine"
          v-model="is_vac"
          class="pt-2"
          :options="['Yes', 'No']"
        ></b-form-radio-group>
      </b-form-group>

      <b-form-group
        label-cols-sm="3"
        label="Contents:"
        label-align-sm="right"
        label-for="nested-contents"
      >
        <b-form-textarea
          id="textarea"
          v-model="contents"
          placeholder="Enter something..."
          rows="6"
          max-rows="9"
        ></b-form-textarea>

        <pre class="mt-3 mb-0">{{ contents }}</pre>
      </b-form-group>

      <b-form-group
        label-cols-sm="3"
        label="Image:"
        label-align-sm="right"
        label-for="nested-contents"
      >
        <b-form-file @change="onFileSelected" v-model="selectedFile" class="mt-3" plain></b-form-file>
        <div class="mt-3">Selected file: {{ selectedFile ? selectedFile.name : '' }}</div>

      </b-form-group>
      <b-form-group
        label-cols-sm="3"
        label="Shelter:"
        label-align-sm="right"
        label-for="nested-shelter"
      >
        <b-form-input id="nested-shelter" v-model="shelter"></b-form-input>
      </b-form-group>
      
      <b-button type="submit" variant="primary">Submit</b-button>
    </b-form-group>
  </b-card>
</div>
</template>

<script>
  export default {
    data() {
      return {
        title:'',
        phone_num:'',
        dog_type:'',
        dog_age:'',
        dog_sex:'',
        is_neu:'',
        is_vac:'',
        contents:'',
        selectedFile:null,
        shelter:'',
      }
    },
    
    methods:{
        onFileSelected(evt){
            this.selectedFile = event.target.files[0]
        },
        onSubmit(evt) {
            evt.preventDefault()
            const fd = new FormData();
            fd.append('title',this.title)
            fd.append('phone_num',this.phone_num)
            fd.append('dog_type',this.dog_type)
            fd.append('dog_age',this.dog_age)
            fd.append('dog_sex',this.dog_sex)
            fd.append('is_neu',this.is_neu)
            fd.append('is_vac',this.is_vac)
            fd.append('contents',this.contents)
            fd.append('image',this.selectedFile,this.selectedFile.name)
            fd.append('shelter',this.shelter)
            this.$http.post('http://202.30.31.91/adopt/post/create', {
            starttime : this.fd,
            
        }).then(res => {
            console.log(res.data)
            this.posts = res.data
        })

        }
    }
  }
</script>