
### request -> entity

    public class BlahBlahRequest {

        private final Long id;
        private final String name;
        private final LocalDateTime createAt;
    
        public BlahBlahEntity toEntity() {
            return new BlahBlahEntity(id, name, createAt);
        }
    }

### entity -> response

    public class BlahBlahResponse {

        private final String name;
        private final LocalDateTime createAt;
    
        public static LiquorElementResponse of(BlahBlahEntity blahBlahEntity) {
            return new LiquorElementResponse(
                blahBlahEntity.getId();
                blahBlahEntity.getName();
                blahBlahEntity.getCreateAt();
            );
        }
    }
