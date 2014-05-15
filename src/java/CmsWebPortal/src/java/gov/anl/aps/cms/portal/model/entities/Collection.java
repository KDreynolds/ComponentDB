package gov.anl.aps.cms.portal.model.entities;

import gov.anl.aps.cms.portal.utilities.ObjectUtility;
import gov.anl.aps.cms.portal.utilities.SearchResult;
import java.text.DecimalFormat;
import java.util.List;
import java.util.regex.Pattern;
import javax.persistence.Basic;
import javax.persistence.CascadeType;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.JoinTable;
import javax.persistence.ManyToMany;
import javax.persistence.ManyToOne;
import javax.persistence.NamedQueries;
import javax.persistence.NamedQuery;
import javax.persistence.OneToMany;
import javax.persistence.Table;
import javax.validation.constraints.NotNull;
import javax.validation.constraints.Size;
import javax.xml.bind.annotation.XmlRootElement;
import javax.xml.bind.annotation.XmlTransient;

/**
 *
 * @author sveseli
 */
@Entity
@Table(name = "collection")
@XmlRootElement
@NamedQueries({
    @NamedQuery(name = "Collection.findAll", query = "SELECT c FROM Collection c"),
    @NamedQuery(name = "Collection.findById", query = "SELECT c FROM Collection c WHERE c.id = :id"),
    @NamedQuery(name = "Collection.findByName", query = "SELECT c FROM Collection c WHERE c.name = :name"),
    @NamedQuery(name = "Collection.findByDescription", query = "SELECT c FROM Collection c WHERE c.description = :description")})
public class Collection extends CloneableEntity
{
    private static final DecimalFormat EstimatedCostDecimalFormat = new DecimalFormat(".00");

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Basic(optional = false)
    @Column(name = "id")
    private Integer id;

    @Basic(optional = false)
    @NotNull
    @Size(min = 1, max = 64)
    @Column(name = "name")
    private String name;

    @Size(max = 256)
    @Column(name = "description")
    private String description;

    @JoinTable(name = "collection_log", joinColumns = {
        @JoinColumn(name = "collection_id", referencedColumnName = "id")}, inverseJoinColumns = {
        @JoinColumn(name = "log_id", referencedColumnName = "id")})
    @ManyToMany(cascade = CascadeType.ALL)
    private List<Log> logList;

    @OneToMany(cascade = CascadeType.ALL, mappedBy = "parentCollection")
    private List<CollectionLink> childCollectionLinkList;

    @OneToMany(cascade = CascadeType.ALL, mappedBy = "childCollection")
    private List<CollectionLink> parentCollectionLinkList;

    @JoinColumn(name = "entity_info_id", referencedColumnName = "id")
    @ManyToOne(cascade = CascadeType.ALL, optional = false)
    private EntityInfo entityInfo;

    @OneToMany(cascade = CascadeType.ALL, mappedBy = "collection")
    private List<CollectionComponent> collectionComponentList;

    private transient Double estimatedComponentCostSum = null;
    private transient Double estimatedComponentCostAverage = null;

    public Collection() {
    }

    public Collection(Integer id) {
        this.id = id;
    }

    public Collection(Integer id, String name) {
        this.id = id;
        this.name = name;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    @XmlTransient
    public List<Log> getLogList() {
        return logList;
    }

    public void setLogList(List<Log> logList) {
        this.logList = logList;
    }

    public EntityInfo getEntityInfo() {
        return entityInfo;
    }

    public void setEntityInfo(EntityInfo entityInfo) {
        this.entityInfo = entityInfo;
    }

    @XmlTransient
    public List<CollectionLink> getChildCollectionLinkList() {
        return childCollectionLinkList;
    }

    public void setChildCollectionLinkList(List<CollectionLink> childCollectionLinkList) {
        this.childCollectionLinkList = childCollectionLinkList;
    }

    @XmlTransient
    public List<CollectionLink> getParentCollectionLinkList() {
        return parentCollectionLinkList;
    }

    public void setParentCollectionLinkList(List<CollectionLink> parentCollectionLinkList) {
        this.parentCollectionLinkList = parentCollectionLinkList;
    }

    @XmlTransient
    public List<CollectionComponent> getCollectionComponentList() {
        return collectionComponentList;
    }

    public void setCollectionComponentList(List<CollectionComponent> collectionComponentList) {
        this.collectionComponentList = collectionComponentList;
    }

    private void calculateCollectionComponentStatistics() {
        estimatedComponentCostSum = 0.0;
        estimatedComponentCostAverage = 0.0;
        for (CollectionComponent collectionComponent : collectionComponentList) {
            Float estimatedCost = collectionComponent.getComponent().getEstimatedCost();
            if (estimatedCost != null) {
                estimatedComponentCostSum += estimatedCost;
            }
        }
        if (!collectionComponentList.isEmpty()) {
            estimatedComponentCostAverage = estimatedComponentCostSum / collectionComponentList.size();
        }
    }

    public Double getEstimatedComponentCostSum() {
        calculateCollectionComponentStatistics();
        return estimatedComponentCostSum;
    }

    public String getDisplayEstimatedComponentCostSum() {
        return "$ " + EstimatedCostDecimalFormat.format(getEstimatedComponentCostSum());
    }
    
    public Double getEstimatedComponentCostAverage() {
        calculateCollectionComponentStatistics();
        return estimatedComponentCostAverage;
    }

    @Override
    public int hashCode() {
        int hash = 0;
        hash += (id != null ? id.hashCode() : 0);
        return hash;
    }

    public boolean equalsByName(Collection other) {
        if (other != null) {
            return ObjectUtility.equals(this.name, other.name);
        }
        return false;
    }

    @Override
    public boolean equals(Object object) {
        if (!(object instanceof Collection)) {
            return false;
        }
        Collection other = (Collection) object;
        if (this.id == null && other.id == null) {
            return equalsByName(other);
        }

        if (this.id == null || other.id == null) {
            return false;
        }
        return this.id.equals(other.id);
    }

    @Override
    public String toString() {
        return name;
    }

    @Override
    public Collection clone() throws CloneNotSupportedException {
        Collection cloned = (Collection) super.clone();
        cloned.id = null;
        cloned.name = "Copy Of " + cloned.name;
        for (CollectionComponent collectionComponent : cloned.collectionComponentList) {
            collectionComponent.setId(null);
            collectionComponent.setCollection(cloned);
        }
        for (CollectionLink collectionLink : cloned.childCollectionLinkList) {
            collectionLink.setId(null);
            collectionLink.setParentCollection(cloned);
        }
        for (CollectionLink collectionLink : cloned.parentCollectionLinkList) {
            collectionLink.setId(null);
            collectionLink.setChildCollection(cloned);
        }
        cloned.entityInfo = null;
        return cloned;
    }
    
    @Override
    public SearchResult search(Pattern searchPattern) {
        SearchResult searchResult = new SearchResult(id, name);
        searchResult.doesValueContainPattern("name", name, searchPattern);
        searchResult.doesValueContainPattern("description", description, searchPattern);
        for (Log logEntry : logList) {
            String logEntryKey = "logEntryId:" + logEntry.getId();
            searchResult.doesValueContainPattern(logEntryKey, logEntry.getText(), searchPattern);
        }
        return searchResult;
    }
    
}
