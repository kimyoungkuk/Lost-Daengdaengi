<template>
<div>
  <b-card bg-variant="light">
    <b-form @submit="onSubmit">
    <b-form-group
      label-cols-lg="3"
      label="유기견 분양글"
      label-size="lg"
      label-class="font-weight-bold pt-0"
      class="mb-0"
    >
      <b-form-group
        label-cols-sm="3"
        label="제목:"
        label-align-sm="right"
        label-for="nested-title"
        invalid-feedback="내용이 입력되지 않았습니다."
      >
        <b-form-input id="nested-title" required v-model="title"></b-form-input>
      </b-form-group>

      <b-form-group
        label-cols-sm="3"
        label="연락처:"
        label-align-sm="right"
        label-for="nested-phone-number"
        invalid-feedback="내용이 입력되지 않았습니다."
      >
        <b-form-input id="nested-phone-number" required v-model="phone_num"></b-form-input>
      </b-form-group>

      <b-form-group
        label-cols-sm="3"
        label="견종:"
        label-align-sm="right"
        label-for="nested-dog-type"
        invalid-feedback="내용이 입력되지 않았습니다."
      >
        <b-form-input id="nested-dog-type" required v-model="dog_type"></b-form-input>
      </b-form-group>

      <b-form-group
        label-cols-sm="3"
        label="연령:"
        label-align-sm="right"
        label-for="nested-dog-age"
        invalid-feedback="내용이 입력되지 않았습니다."
      >
        <b-form-input id="nested-dog-age" required v-model="dog_age"></b-form-input>
      </b-form-group>

      <b-form-group
        label-cols-sm="3"
        label="성별:"
        label-align-sm="right"
        label-for="nested-dog-sex"
        invalid-feedback="내용이 선택되지 않았습니다."
      >
        <b-form-radio-group
          id="dog-sex"
          required
          v-model="dog_sex"
          class="pt-2"
          :options="[{text:'수컷', value:1}, {text:'암컷', value:2}]"
        >
        </b-form-radio-group>
      </b-form-group>

      <b-form-group
        label-cols-sm="3"
        label="중성화:"
        label-align-sm="right"
        label-for="nested-neutralizer"
        invalid-feedback="내용이 선택되지 않았습니다."
      >
        <b-form-radio-group
          id="nested-neutralizer"
          required
          v-model="is_neu"
          class="pt-2"
          :options="['O', 'X']"
        ></b-form-radio-group>
      </b-form-group>

      <b-form-group
        label-cols-sm="3"
        label="예방접종:"
        label-align-sm="right"
        label-for="nested-vaccine"
        invalid-feedback="내용이 선택되지 않았습니다."
      >
        <b-form-radio-group
          id="nested-vaccine"
          required
          v-model="is_vac"
          class="pt-2"
          :options="['O', 'X']"
        ></b-form-radio-group>
      </b-form-group>

      <b-form-group
        label-cols-sm="3"
        label="내용:"
        label-align-sm="right"
        label-for="nested-contents"
        invalid-feedback="내용이 입력되지 않았습니다."
      >
        <b-form-textarea
          id="textarea"
          required
          v-model="contents"
          placeholder="소개글을 적어주세요"
          rows="6"
          max-rows="9"
        ></b-form-textarea>

        <pre class="mt-3 mb-0">{{ contents }}</pre>
      </b-form-group>

      <b-form-group
        label-cols-sm="3"
        label="이미지:"
        label-align-sm="right"
        label-for="nested-contents"
        invalid-feedback="파일이 선택되지 않았습니다."
      >
        <b-form-file required  @change="onFileSelected" v-model="selectedFile" class="mt-3" plain></b-form-file>
        <div class="mt-3">선택된 이미지: {{ selectedFile ? selectedFile.name : '' }}</div>

      </b-form-group>
      <b-form-group
        label-cols-sm="3"
        label="보호소:"
        label-align-sm="right"
        label-for="nested-shelter"
        invalid-feedback="내용이 입력되지 않았습니다."
      >
        <b-form-select id="nested-shelter" required v-model="shelter" :options="options"></b-form-select>
      </b-form-group>
      
      <b-button type="submit" variant="primary">Submit</b-button>
    </b-form-group>
    </b-form>
  </b-card>
</div>
</template>

<script>
  export default {
    data() {
      return {
        selectedFile:null,
        title:'',
        phone_num:'',
        dog_type:'',
        dog_age:'',
        dog_sex:'',
        is_neu:'',
        is_vac:'',
        contents:'',
        image:'',
        imageurl:'',
        shelter:'',
        options: [
          { value: '대전광역시 동물보호센터', text: '대전광역시 동물보호센터' },
          { value: '반송원', text: '반송원' },
          { value: '용인시 동물보호센터', text: '용인시 동물보호센터' },
          { value: '아산천사원유기견보호소', text: '아산천사원유기견보호소' },
          { value: '영암 유기견보호소', text: '영암 유기견보호소' },
          { value: '반려동물과함께하는내사랑바둑이', text: '반려동물과함께하는내사랑바둑이' },
          { value: '남양동물보호센터', text: '남양동물보호센터' },
          { value: '나나우리봉사단', text: '나나우리봉사단' },
          { value: '대관령동물병원', text: '대관령동물병원' },
          { value: '대장마을협동조합 반려동물놀이터', text: '대장마을협동조합 반려동물놀이터' }
        ]
      }
    },
    methods:{
        onFileSelected(evt){
            this.selectedFile = event.target.files[0]
            let temp=encodeBase64ImageFile(this.selectedFile)
            temp.then((data)=>{
                console.log(data)
                this.image=data
            })
        },
        onSubmit(evt) {
            evt.preventDefault()
            
            this.$http.post('http://202.30.31.91:8000/adopt/post/create', {
            title:this.title,
            phone_num:this.phone_num,
            dog_type:this.dog_type,
            dog_age:this.dog_age,
            dog_sex:this.dog_sex,
            is_neu:this.is_neu,
            is_vac:this.is_vac,
            contents:this.contents,
            image:this.image,
            imageurl:this.imageurl,
            shelter:this.shelter,
            user_nickname:this.$store.state.user_nickname,

        }).then(res => {
            
            
            console.log("QWE")
            console.log(res.data)
            console.log("QWE")
            this.$router.push("/adopt/post/list?is=a");
            // this.posts = res.data
        })

        }
    }
  }

function encodeBase64ImageFile (image) {
  return new Promise((resolve, reject) => {
    let reader = new FileReader()
    // convert the file to base64 text
    reader.readAsDataURL(image)
    // on reader load somthing...
    reader.onload = (event) => {
      resolve(event.target.result)
    }
    reader.onerror = (error) => {
      reject(error)
    }
  })
}
</script>